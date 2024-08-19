from openai import OpenAI
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import os
import tkinter as tk
from tkinter import ttk
from forResume import allPrompts, projects_info, cover_letter_template, question1, question2, question3, allPrompts2, question1_2
from resClass import promptArr, sevenLineProjects
import os
import asyncio
import ast
from datetime import datetime
import pytz
from dotenv import load_dotenv
load_dotenv()


openai_key = os.getenv('OPENAI_KEY')
SCOPES = ['https://www.googleapis.com/auth/drive']

client = OpenAI()


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


async def select_inputs(job_info):
    messages = [
        # {"role": "user", "content": f"{allPrompts} {job_info}. {question1}"},
        {"role": "user", "content": f"{question1_2} \n Prompts: {allPrompts2}  \n Job Description:{job_info}"},
        {"role": "user", "content": f"{question2} \n Projects: {projects_info} \n Job Description: {job_info}. "},
        {"role": "user", "content": f"{question3} \n Cover Letter Template: {cover_letter_template} \n Job Description: {job_info}"},
        {"role": "user", "content": '''Return the prompt numbers,project numbers, and inputs for the cover letter template in 3 arrays and nothing else(USE DOUBLE QUOTES FOR EACH VALUE IN THE ARRAY). For example it should look like this(all on the same line and also remove the curly brackets in your answer): ["prompt1", "prompt2", "prompt3", "prompt4", "prompt5", "prompt6", "prompt7", "prompt8],["project1", "project2", "project3"]["{Today's Date(eg. May 31st, 2024)}", "{Company Name}", "{Location of job(eg. Toronto, Ontario)}", etc..]'''}
    ]
    completion = client.chat.completions.create(
    model="gpt-4o", 
    messages=messages,
    max_tokens=300,  
    temperature=1,  
    )

    message_content = completion.choices[0].message.content
    print(message_content)

    prompt_indices, project_indices, cv_indices = eval(message_content)

    prompt_indices = [int(x) for x in prompt_indices]
    project_indices = [int(x) for x in project_indices]
    cv_indices = [str(x) for x in cv_indices]

    return prompt_indices, project_indices, cv_indices


def update_application_counts():
    today_date_str = datetime.now().strftime('%Y-%m-%d')
    with open('applicationsSent.json', 'r+') as file:
        data = json.load(file)

        if data["last_updated"] != today_date_str:
            data["total_applications_sent_today"] = 0
            data["last_updated"] = today_date_str
      
        data["total_applications_sent_today"] += 1
        data["total_applications_sent"] += 1

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

        totalAppsLabel.config(text=f"Total Applications Sent: {data['total_applications_sent']}")
        totalAppsTodayLabel.config(text=f"Applications Sent Today: {data['total_applications_sent_today']}")
def get_initial_app_counts():
    with open('applicationsSent.json', 'r') as file:
        return json.load(file)

def authenticate_google_docs():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

async def update_resume_doc(prompt_indices, project_indices, cv_indices):

    eastern = pytz.timezone('America/Toronto')
    today_toronto = datetime.now(eastern)
    formatted_date = custom_strftime('%B {S}, %Y', today_toronto)
    print(formatted_date)

    print('Creating tailored resume and cover letter...')
    creds = authenticate_google_docs()

    service = build('docs', 'v1', credentials=creds)
    service2 = build('drive', 'v3', credentials=creds)

    copy_file_res = {
        'name': f"{cv_indices[1]} {cv_indices[3]} - Resume"
    }
    copy_file_cv = {
        'name': f"{cv_indices[1]} {cv_indices[3]} - Cover Letter"
    }

    # resume_file_id = '1Fr3qlYlxdYNy2igNGdWTM2BUrbSBv7X3xl8ADrfgQlQ' <- This is V3
    resume_file_id = '1rdjKMllM-Hgj1XzLHsTyn4XDmeU4W3NY1gIxQh5fBlc' # <- This is V4
    cv_file_id = '1I6gqnb4i5B-4qf7mw6TCkoZT9m1dhPDbc8GFRTT04jM'

    resume_requests = [
         {
            'replaceAllText': {
                'containsText': {
                    'text': '{{1-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[0]],
            }}, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{2-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[1]],
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{3-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[2]],
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{4-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[3]],
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{5-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[4]],
            }
        }, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{6-2line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[5]],
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{7-1line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[6]],
            }
        }
        , 
        {
            'replaceAllText': {
                'containsText': {
                    'text': '{{8-1line-prompt}}',
                    'matchCase':  'true'
                },
                'replaceText': promptArr[prompt_indices[7]],
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project1-title}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[0]].title,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project1-date}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[0]].date,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project1-bullet1}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[0]].bullet1,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project1-bullet2}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[0]].bullet2,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project1-bullet3}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[0]].bullet3,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project2-title}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[1]].title,
            }
        }
        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project2-date}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[1]].date,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project2-bullet1}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[1]].bullet1,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project2-bullet2}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[1]].bullet2,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project2-bullet3}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[1]].bullet3,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project3-title}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[2]].title,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project4-date}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[2]].date,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project3-bullet1}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[2]].bullet1,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project3-bullet2}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[2]].bullet2,
            }
        }        , {
            'replaceAllText': {
                'containsText': {
                    'text': '{{project3-bullet3}}',
                    'matchCase':  'true'
                },
                'replaceText': sevenLineProjects[project_indices[2]].bullet3,
            }
        } 
    ]

    cover_letter_requests = [
            {
            'replaceAllText': {
                'containsText': {
                    'text': '{{Todays Date in the form like - May 31st, 2024}}',
                    'matchCase':  'true'
                },
                'replaceText': formatted_date,
            }}, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{Company Name}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[1],
            }
        },
                    {
            'replaceAllText': {
                'containsText': {
                    'text': '{{Location of job(eg. Toronto, Ontario)}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[2],
            }}, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{Job Title}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[3],
            }
        },
                            {
            'replaceAllText': {
                'containsText': {
                    'text': '{{1-2 sentences of why you want to work here and what makes them special to you - make this part personal and unique, avoid giving blank and boring answers}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[4],
            }}, {
            'replaceAllText': {
                'containsText': {
                    'text': '{{specific skill or technology}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[5],
            }
        },
        {
            'replaceAllText': {
                'containsText': {
                    'text': '{{specific contribution to the company}}',
                    'matchCase':  'true'
                },
                'replaceText': cv_indices[6],
            }
        },
        
        
    ]


    try:
        new__res_file = service2.files().copy(fileId=resume_file_id, body=copy_file_res).execute()
        new_res_file_id = new__res_file.get('id')
        result = service.documents().batchUpdate(
        documentId=new_res_file_id, body={'requests': resume_requests}).execute()
        print('Successfully created resume doc!')


        new_cv_file = service2.files().copy(fileId=cv_file_id, body=copy_file_cv).execute()
        new_cv_file_id = new_cv_file.get('id')
        result2 = service.documents().batchUpdate(
        documentId=new_cv_file_id, body={'requests': cover_letter_requests}).execute()
        print('Successfully created cover letter doc!')
        update_application_counts()

    except Exception as e:
        print(f'An error occurred: {e}')

def start():
    progress_bar.start(10)
    job_info = text_area.get("1.0", "end-1c")
    print(f"job info here is {job_info}")
    prompt_indices, project_indices, cv_indices = asyncio.run(select_inputs(job_info))
    asyncio.run(update_resume_doc(prompt_indices,project_indices, cv_indices))
    progress_bar.stop()

root = tk.Tk()
root.minsize(400, 600)

initial_data = get_initial_app_counts()
appsSent = initial_data["total_applications_sent"]
appsSentToday = initial_data["total_applications_sent_today"]
root.title('AI Automated Resume/Cover Letter Generator')
root.geometry("600x400")

progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=200)
progress_bar.grid(row=3, column=0, padx=10, pady=10)
label = tk.Label(root, text='This is an AI automated Resume/Cover Letter generator. This application uses the job information you provide below to best match projects/prompts for your resume. It also generates personal sentences to your cover letter. It uses both the Google Drive API and OpenAI API(Using GPT-4 Model) to acccomplish this. Please add your job information below.', wraplength=550, justify="left")
label.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky=(tk.W, tk.E))

totalAppsLabel = tk.Label(root, text=f"Total Applications Sent: {appsSent}")
totalAppsTodayLabel = tk.Label(root, text=f"Applications Sent Today: {appsSentToday}")
totalAppsLabel.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky=(tk.W, tk.E))
totalAppsTodayLabel.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky=(tk.W, tk.E))

text_area = tk.Text(root, wrap='word', height=15, width=50)
text_area.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

job_info = text_area.get("1.0", tk.END)
# print(f"job info here is {job_info}")
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_area.yview)
scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

text_area['yscrollcommand'] = scrollbar.set
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

button = tk.Button(root, text="Generate Resume/CV", command=start)
button.grid(row=2, column=0, columnspan=2, pady=20)
root.mainloop()
# update_resume_doc(prompt_indices, project_indices, cv_indices)

