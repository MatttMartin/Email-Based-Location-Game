import imaplib, email

def get_vars(x):
    user = 'pythontestemail74@gmail.com'
    password = 'neweublczzgazsup'
    imap_url = 'imap.gmail.com'

    con = imaplib.IMAP4_SSL(imap_url)

    if x == 'user':
        return user
    elif x == 'password':
        return password
    elif x == 'imap_url':
        return imap_url
    elif x == 'con':
        return con
    elif x == 'all':
        return user, password, imap_url, con


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))

    else:
        return msg.get_payload(None, True)

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data


def get_email_ints(sender, con):
    results = (search('FROM', sender, con)[0]).split()
    numbers = []
    for result in results:
        numbers.append(int(result.decode("utf-8")))

    return numbers
    

def get_latest_email_byte(sender, con):
    numbers = get_email_ints(sender, con)
    return bytes(str(max(numbers)), 'utf-8')

    
        
def get_latest_body(sender):
    user, password, imap_url, con = get_vars('all')
    
    con.login(user, password)
    con.select('INBOX')

    byte = get_latest_email_byte(sender, con)
    result, data = con.fetch(byte, '(RFC822)')
    raw = email.message_from_bytes(data[0][1])

    string = get_body(raw).decode("utf-8")
    return string.strip()



def check_for_new_email(sender):
    user, password, imap_url, con = get_vars('all')
    
    con.login(user, password)
    con.select('INBOX')

    
    f = open('{}.txt'.format(sender), 'a+')#creates file if it doesnt exist yet
    f.close()
    
    f = open('{}.txt'.format(sender), 'r')
    f_contents = f.read()
    f.close()

    if f_contents == '':
        f = open('{}.txt'.format(sender), 'r+')
        f.write('0')
        f_contents = '0'
        f.close()
    
    number_of_emails = len(get_email_ints(sender, con))
    if number_of_emails > int(f_contents):
        f = open('{}.txt'.format(sender), 'w')
        f.write(str(number_of_emails))
        f.close()
        return True
    else:
        return False
        





def main():
    print('results: {}'.format(get_latest_body('matthew.g.martin@ryerson.ca')))
    print(check_for_new_email('mglm8650@gmail.com'))

if __name__ == '__main__':
    main()

    

