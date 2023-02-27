import asyncio

async def process(reader, writer):
    while True:
        data = await reader.readline()
        if not data:
            break
        writer.write(b'HTTP/1.1 200 OK\r\n\r\n')

loop = asyncio.get_event_loop()
listener = asyncio.start_server(process, host='0.0.0.0', port=11000)
loop.run_until_complete(listener)
loop.run_forever()

