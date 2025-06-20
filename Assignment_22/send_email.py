import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def Send_Email(FileName,SenderAddress,TotalFileScanned,TotalDeleted,starttime):
# Sender and receiver information
    fromaddr = "akshaykhopade1505@gmail.com"
    toaddr = SenderAddress
    password = "ygbb hjrg jdwf fxog"  # Use app password if using Gmail

# Create message object
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File Report"

# Email body
    body = "Report generated on: " + str(starttime) + "\n" + "Total files scanned: " + str(TotalFileScanned) + "\n" +"Total duplicate files deleted: " + str(TotalDeleted)
# Attach body to message
    msg.attach(MIMEText(body, 'plain'))

# File to attach
    filepath = FileName
    filename = os.path.basename(FileName)
    print(filename)


# Open file in binary mode and attach   
    attachment = open(filepath, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)
    attachment.close()

# Create SMTP session (TLS)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    print("Email sent successfully with attachment.")

    
# Send_Email("/home/pawar/Desktop/Python_Assignments/Assignment_21/Marvellous/Marvellous.log")