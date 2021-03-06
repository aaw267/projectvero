projectvero

# Project Vero

Blockchain Application for Proving News Truth

## Dependencies

- Flask >= 0.12.2
- Python >= 3
- requests >= 2.18.4

## Commands

If using pyenv:
`{$PROJECT_PATH}/projectvero/venv/bin/python -m flask run`

If using global python path:
`python -m flask run`

## Git Commands

 `git status` to see if you've made changes. <br>
 `git fetch` to see if there are any updates from the "origin"<br>
 `git pull` to pull the updates down and merge them into your branch.** If you're on the same branch

<br>

`git add .` to commit all changes. Might need to .gitingore some things.<br>
`git commit` to commit your changes.<br>
`git push` to push your changes to the origin.<br>
`git reset HEAD --hard` resets all code with no saves to your previous head.<br>
`git log` shows you the commit log.<br>
`Q` to get out of git log.<br>

## curl POST Command

```bash
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```
OR <br>
```bash
curl -X POST -H "Content-Type: application/json" -d '{
 "nodes": {"http://127.0.0.1:5001"} 
}' "http://localhost:5000/nodes/register
```

## curl GET Commands
`curl http://localhost:5000/mine`<br>
OR <br>
`curl http://localhost:5000/chain`<br>
OR <br>
`curl http://localhost:5000/resolve`
