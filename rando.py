import recieveEmail
import sendEmail
import coords
import time

sub = 'Randonaut'
change_email_key = 'change email to'
get_coords_key = 'rando time'
help_key = 'help'
body = ''


def get_coords(coord1, coord2):
    
    return 'hello hello hello helloooo'

while 1:
    f = open('current_email.txt', 'r')
    sender = f.read()
    f.close()
    
    if recieveEmail.check_for_new_email(sender):
        body_recieved = ((((recieveEmail.get_latest_body(sender).lower()).replace(',', '')).replace(')', '')).replace('(', '')).split(' ')
        print('recieved request: {}'.format(body_recieved))

        try:
            if body_recieved[:len((change_email_key).split(' '))] == change_email_key.split(' '):
                newEmail = body_recieved[len((change_email_key).split(' '))]
                body = 'Email has successfully been changed.\nOnly {} will have access to randonaut now.'.format(newEmail)
                sendEmail.email_alert(sub, body, sender)
                
                sender = newEmail
                f = open('current_email.txt', 'w')
                f.write(newEmail)
                f.close()
                
                body = 'You have been given access to randonaut.\nSend \'help\' to this email for instructions.'
                sendEmail.email_alert(sub, body, sender)
                print('new email is {}'.format(sender))
            
            elif body_recieved[:len((get_coords_key).split(' '))] == get_coords_key.split(' '):
                lat, long, distance = float(body_recieved[len((get_coords_key).split(' '))]), float(body_recieved[len((get_coords_key).split(' ')) + 1]), float(body_recieved[len((get_coords_key).split(' ')) + 2])
                output_lat, output_long = coords.get_coords(lat, long, distance)
                
                body = 'Your coordinates to find are: {}, {}\nHappy randonauting'.format(output_lat, output_long)
                sendEmail.email_alert(sub, body, sender)
                print('sent coordinates: {}, {}'.format(output_lat, output_long))

            elif body_recieved[0] == help_key:
                body = 'Instructions: Email the following commands to this email\nTo be sent coordinates: rando time (your current latitude), (your current longitude), (range)\nTo pass off the game to another email: change email to (email)\nTo get to this help page: help'
                sendEmail.email_alert(sub, body, sender)
                print('sent help')

            else:
                body = 'Invalid command. Send \'help\' to this email for instructions.'
                sendEmail.email_alert(sub, body, sender)
                print('sent error message')

        except:
            body = 'ERROR. Send \'help\' to this email for instructions.'
            sendEmail.email_alert(sub, body, sender)
            print('sent critical error message')   
            
        
        

        
        
    time.sleep(1)
    
