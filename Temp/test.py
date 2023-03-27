# Import the following modules
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import time

# Get the access token from Pushbullet.com
access_token = "o.iWpCF5YUOnRQptu222OYh4XYzz7yIn31"


# Taking input from the user
#data = input('Title')
data= 'Sachin'

# Taking large text input from the user
'''text = textarea(
"Text", rows=3, placeholder="Write something...",
required=True)'''

text= 'Hello my friend'

# Get the instance using access token
pb = PushBullet(access_token)

# Send the data by passing the main title
# and text to be send
push = pb.push_note(data, text)

# Put a success message after sending
# the notification
put_success("Message sent successfully...")

# Sleep for 3 seconds
time.sleep(3)

# Clear the screen
clear()

# Give the pop at last
toast("Thanks for using it :)")

# hold the session until the whole work finishes
#hold()
