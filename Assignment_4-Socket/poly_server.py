import polynomials
import socket

port=12345
# 1. create a socket
listener=socket.socket()
# 2. bind the socket with IP address and port number
listener.bind(('',port))
# 3. generate a listener
listener.listen(15)


def end_connection(response_tag, result, sock):
    response = f"{response_tag}{result}"
    # print(f"{response}")
    resp_byte = response.encode(encoding='UTF-16',errors='strict')

    sock.sendall(resp_byte)

    sock.shutdown(1)  # signal close of the writing side of the socket

    sock.close()


def string_to_float_error(val):
    return f"Could not convert string to float: '{val}'"


def too_few_args_error():
    return "Too few arguments."


def incorrect_command_error():
    return "Incorrect command type."

def invalid_tolerance():
    return "Invalid tolerance"


while True:
    result = ""
    response_tag = ""
    (sock,address) = listener.accept()
    print(address)
    bytes = sock.recv(2048)
    client_data = ""


    while len(bytes) > 0:
        client_data += bytes.decode(encoding='UTF-16',errors='strict')
        print("client data: " + client_data)
        bytes = sock.recv(2048)
        
        data = client_data.split()
        x = None

        if "E" in data[0]:
            response_tag = "E"
            try:
                x = float(data[0].replace("E", ""))
            except BaseException:
                result = string_to_float_error(data[0].replace("E", ""))
                print(result)
                end_connection(response_tag="X", result=result, sock=sock)

            if len(data) <= 1:
                result = too_few_args_error()
                end_connection(response_tag="X", result=result, sock=sock)

            # data[0] = float(data[0].replace("E",""))
            data.pop(0)
            i = 0
            while i < len(data):
                try:
                    data[i] = float(data[i])
                except:
                    result = string_to_float_error(data[i])
                    end_connection(response_tag="X", result=result, sock=sock)
                    exit(0)
                i += 1
                try:
                    result = polynomials.evaluate(x, data)
                except:
                    break

        elif "S" in data[0]:
            response_tag = "S"
            try:
                a = float(data[0].replace("S", ""))
                data[0] = a
            except:
                result = string_to_float_error(data[0].replace("S", ""))
                end_connection(response_tag="X",result=result, sock=sock)

            try:
                b = data[1]
            except:
                result = too_few_args_error()
                end_connection(response_tag="X", result=result, sock=sock)
            try:
                b = float(data[1])
            except:
                result = string_to_float_error(data[1])
                end_connection(response_tag="X", result=result, sock=sock)

            try:
                tolerance = float(data[len(data)-1])
                if tolerance < 0:
                    result = invalid_tolerance()
                    end_connection(response_tag="X", result=result, sock=sock)
            except:
                result = string_to_float_error(data[len(data)-1])
                end_connection(response_tag="X", result=result, sock=sock)

            data.pop()
            i = 0
            while i < len(data):
                try:
                    data[i] = float(data[i])
                    i += 1
                except:
                    result = string_to_float_error(data[i])
                    end_connection(response_tag="X", result=result, sock=sock)

            result = f"{polynomials.bisection(a,b,data,tolerance)}"
            response_byte = result.encode()
            sock.sendall(response_byte)

        else:
            result = incorrect_command_error()
            end_connection(response_tag="X", result=result, sock=sock)

    # sock.shutdown(1)  # signal close of the writing side of the socket

    # sock.close()