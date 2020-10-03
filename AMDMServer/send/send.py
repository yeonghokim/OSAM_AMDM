def sendMessage(message,sock):
    sock.send(message.encode('utf-8'))

def sendMessageJson(message,sock):
    sock.send(message.encode('utf-8'))