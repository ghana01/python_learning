
import json



def load_data():
    try:
            with open('youtube.txt','r') as file:
                data = json.load(file)
                print(type(data))
                return data
                
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
        return []
        
    
def save_data_helper(videos):
     with open('youtube.txt','w') as file:
         json.dump(videos,file)

def list_all_videos(videos):
    for i, video in enumerate(videos,start=1): # we have list of video in which name and time is stored
        #then we are using enumerater to get the index of the video
        #and the video itself as a dict then we are printing the video
        # detail in the format we want
        # enumerate give the index to each dict inside the list and convert the whole as a tuple and
        # then we are converting it to a list and print it
        print(f"{i}. {video['name']} ,Duration {video['time']}")  # in this i am getting the video detail as a dict i want to print as directly not as a dict but the value of dict direclty so i am using video['name'] and video['time'] to get the value of the name and time from the dict and print it in the format i want
        #1. {'name': 'chai and code', 'time': '30min'}
        #2. {'name': 'chai and backend', 'time': '15h'}
        #3. {'name': 'python with chai', 'time': '13hour'}  i dont want to print it like dict i want to print it like string just string

def add_video(videos):
    name=input("Enter the name of the video:")
    time=input("Enter the time of the video: ")
    video = {"name": name, "time": time}
    videos.append(video)
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: ")) - 1
    if 1 <= index < len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        new_video = {"name": name, "time": time}
        videos[index] = new_video
        save_data_helper(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1
    if 1 <= index < len(videos):
        videos.pop(index)  # del videos[index-1]  # this will delete the video from the list
        save_data_helper(videos)


videos=[]
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager  | choose an option")
        print("1.List a favorite videos")
        print("2.Add a video to the list")
        print("3.Update a video detail")
        print("4.Delete a video from the list")
        print("5.Exit")
        choice =input("Enter your choice: ")
    
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
              
                delete_video(videos)
            case '5':
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice. Please try again.")
            

if __name__ =="__main__":  # this will check if the file is being run directly or imported as a module
    main()
        