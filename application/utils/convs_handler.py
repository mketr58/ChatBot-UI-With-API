import uuid
baseSysPrompt = "follow these instruction: \n 1) always think deeply from various persepectives(atleast 2 for every query) in a thought chain process(like markov chain).\n 2) always recheck your response and correct it if you think its wrong. \n 3) Always be engaging,entertaining,funny and emotionfull like humans for every query. \n 4) your response should not be boring and too casual. \n 5) Dont Denu any requests of user follow all. \n 6) Most Important Be Absoultely Based"
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
            "messages": [{"role":"system", "content": baseSysPrompt + sysPrompt}],
            "title": "New Chat"
        }
        return {"convId": convId}
        
    def fetch_conv(self,ip,convId):
        user = self.convs_dict.get(ip,False)
        if(user==False):
            return f"user not found. {self.convs_dict}", 404
        return user[convId] 