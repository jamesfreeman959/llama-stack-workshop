import os
import requests
from datetime import datetime

from llama_stack_client.types.shared.document import ContentTextContentItem, Document

# Fetch the JSON schedule data
url = "https://pretalx.devconf.info/devconf-cz-2025/schedule/v/0.4.10/widgets/schedule.json"
response = requests.get(url)
schedule_data = response.json()

# Extract speakers and tracks from the schedule data
speakers = {speaker['code']: speaker['name'] for speaker in schedule_data['speakers']}
tracks = {track['id']: track['name']['en'] for track in schedule_data['tracks']}

# Create a directory to store the Markdown files
output_dir = "../resources/dev_conf_cz_2025_talks"
os.makedirs(output_dir, exist_ok=True)

# Iterate through each talk and generate a Markdown file
for talk in schedule_data['talks']:
    if 'code' not in talk:
        continue

    talk_code = talk['code']
    title = talk['title']
    abstract = talk['abstract']
    speaker_codes = talk['speakers']
    track_code = talk['track']
    room = talk['room']
    start_time = datetime.fromisoformat(talk['start'])
    end_time = datetime.fromisoformat(talk['end'])
    duration = (end_time - start_time).seconds // 60  # Duration in minutes

    # Resolve speaker names
    speaker_names = [speakers[code] for code in speaker_codes]

    # Resolve track name
    track_name = tracks.get(track_code, "Unknown Track")

    # Format the start time
    formatted_start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

    # Prepare the content for the Markdown file
    md_content = f"""# {title}

**Speakers:** {', '.join(speaker_names)}
                    
**Track:** {track_name}
                    
**Room:** {room}
                    
**Date & Time:** {formatted_start_time}
                    
**Duration:** {duration} minutes
                    
## Abstract
                    
{abstract}
"""

    # Define the path for the Markdown file
    md_file_path = os.path.join(output_dir, f"{talk_code}.md")

    # Write the content to the Markdown file
    with open(md_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

    print(f"Generated Markdown file for talk: {title}")

print("All Markdown files have been generated.")


def fetch_dev_conf_talks_md():
    documents = []

    for filename in os.listdir(output_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            document_id = os.path.splitext(filename)[0] # Remove .md extension
            document = Document(
                document_id=document_id,
                content=ContentTextContentItem(text=content, type="text"),
                mime_type="text/plain",
                metadata={

                },
            )
            documents.append(document)
    return documents