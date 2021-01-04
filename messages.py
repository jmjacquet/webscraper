from win10toast import ToastNotifier 
toaster = ToastNotifier()
header = 'Medium Article'
text = 'Its the correct time to start writing your article'
toaster.show_toast(f"{header}",f"{text}",duration=10,threaded=True)
while toaster.notification_active(): time.sleep(0.005)   