import urllib.request, json

def get_repositories(org):
    """List all names of GitHub repositories for an org."""
    url = "https://api.github.com/orgs/{}/repos".format(org)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]      

    #List comprehension
    #return [repo['name'] for repo in data] 

   