import requests;
from base64 import b64encode

basePath = 'http://localhost:8085/kie-server';

def _header():
    return {'Authorization': 'Basic '+ b64encode(f"wbadmin:wbadmin".encode('utf-8')).decode("ascii"), 'accept': 'application/json'};


def _container():
    url = basePath + '/services/rest/server/containers';
    response = requests.get(url, headers=_header());
    print('Fetched containers status :: ', response.status_code)

    res = response.json()
    containers =  res.get('result').get('kie-containers').get('kie-container');
    if(len(containers) == 0) :
        print('Skipped to check active process, as no containers found !')
        return;
    
    for c in containers:
        id = c.get('container-id');
        if(_hasActiveProcess(id)):
            print('Found that their is no active conatiner for ::', id)
            _delete(id);
            break;

def _hasActiveProcess(containerid: str):
    url = basePath + '/services/rest/server/containers/'+containerid+'/processes/instances?page=0&pageSize=1&sortOrder=true';
    response = requests.get(url, headers=_header());
    print('Fetched process status :: ', response.status_code)
    res = response.json()
    if(len(res.get('process-instance')) != 0) :
        print('Active process found for container ::', containerid)
        return False;
    else :
        return True;

def _delete(containerid: str):
    url = basePath + '/services/rest/server/containers/'+containerid;
    response = requests.delete(url, headers=_header());
    res = response.json()
    print(res.get('msg'));

if __name__ == "__main__":
    print('========== START DISPOSED =============')
    _container()
    print('========== END DISPOSED =============')
