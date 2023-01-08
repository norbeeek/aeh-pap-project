from website import create_app
import ssl

app = create_app()

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('D:\Python projects\AEH\MySQL\cert.pem','D:\Python projects\AEH\MySQL\key.pem')
    app.run(host='0.0.0.0', port='443', ssl_context=context)