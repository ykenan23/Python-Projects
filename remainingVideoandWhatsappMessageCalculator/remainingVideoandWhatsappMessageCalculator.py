

def main():

    #This will convert input package quota to mb and then sends to kb_convertor function. 
    package_quota = float(input("Please enter your internet quota (GB): "))
    video_time_counter = int(input("Please enter your total video viewing time in minutes: "))
    message_counter = int(input("Please enter your number of messages you send: "))
    mb=float(package_quota*1024)
    kb_converter(mb,video_time_counter,message_counter)

    degisken1=str("ece")
    print(degisken1)

def kb_converter(mb,video_time_counter,message_counter):

    #This will mb size to kb and decrease the message and video using data from quota. Then calls the gb_converter function.

    kb=float(mb*1024)
    print(str(kb))

    #each video at minute 7.7 Mb = 7884.8 Kb
    #each Whatsapp message 1.7 kb

    package_quota_kb=kb-float(video_time_counter*7884.8)
    package_quota_kb=package_quota_kb-float(message_counter*1.7)
    gb_converter(package_quota_kb)

def gb_converter(kb):

    #This will prepare the result for writing to screen and write then checks the plan for mobile data spent. 
    #If enough shows to remaining quota with Gb(s) float value. Then call the last remaining_video_calculator function.
    #If not enough it wants the inputs from the user again.

    mb=float(kb/1024)
    gb=float(mb/1024)
    gb=round(gb,2)
    gb=str(gb)
    if(float(kb)<=0):
        print("Your internet quota is not enough for those. Please enter values again: ")
        main()
    else:
        print("Your remaining internet quota is " + gb + "gb(s)")
        remaining_video_calculator(kb)

def remaining_video_calculator(kb):
    #This will prints how many hours, minutes and seconds play video at 480p with remaining data quota

    #each video at second estimate 131.4 Kb

    total_seconds=float(kb)//131.4
    hour = total_seconds // 3600
    hour=int(hour)
    total_seconds %= 3600
    minutes = total_seconds // 60
    minutes=int(minutes)
    total_seconds %= 60
    seconds = total_seconds
    seconds=int(seconds)
    print("You can watch video for "+ str(hour) + " hour(s), "+ str(minutes) + " minute(s), " + str(seconds) + " second(s).")


main()
