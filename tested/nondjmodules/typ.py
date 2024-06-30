def typer(filename:str) -> str:
	match filename.split('.')[-1]:
		case 'css':
			return 'text/css'
		case 'js':
			return 'text/javascript'
		case _:
			return 'text/plain'