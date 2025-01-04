import uuid
class ConvHandler:
    def __init__(self,convs_dict):
        self.convs_dict = convs_dict;

    def get_conv(self,ip):
        if(ip not in self.convs_dict):
            self.convs_dict[ip] = {"metadata": []}
        return self.convs_dict[ip]['metadata']

    def create_conv(self,ip,sysPrompt):
        user = self.convs_dict.get(ip,False)
        if(user==False):
            return f"user not found. {self.convs_dict}", 404
        convId = str(uuid.uuid4())
        user[convId] = {
            "messages": [{"role":"system", "content": sysPrompt}],
            "title": "New Chat"
        }
        return {"convId": convId}
        
    def fetch_conv(self,ip,convId):
        user = self.convs_dict.get(ip,False)
        if(user==False):
            return f"user not found. {self.convs_dict}", 404
        return user[convId] 