from youtube_transcript_api import YouTubeTranscriptApi

def save_subtitles_to_txt(video_id, filename, languages=['ru']):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        with open(filename, 'w', encoding='utf-8') as file:
            for transcript in transcript_list:
                file.write(transcript['text'] + '\n')
        print("Subtitles saved to", filename)
    except Exception as e:
        print("Error occurred:", e)

# Пример использования
video_id = 'fn1zQj02qN0'
filename = 'subtitles.txt'
save_subtitles_to_txt(video_id, filename)