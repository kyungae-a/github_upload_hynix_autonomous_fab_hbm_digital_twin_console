from pathlib import Path
for d in ['outputs','release','screenshots']:
 Path(d).mkdir(exist_ok=True)
print('PASS setup')
