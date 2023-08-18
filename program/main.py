from func_connections import connect_dydx

if __name__ == "__main__":
    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print("Error connecting to client: ", e)
        exit(1)