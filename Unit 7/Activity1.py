rooms = {}


def createRoom(name):
    rooms[name] = {}
    return rooms


def createAsset(room, assetName, price):
    if room in rooms:
        rooms[room][assetName] = price
        return rooms
    return "Error - no such room exists yet."


accounts = {}
places = {}


def createAccount(username):
    if username in accounts:
        return "Error - Account already exists."
    else:
        accounts[username] = {}
        return f"Account created for {username}."


def createPlace(username, placeName):
    if username not in accounts:
        return "Error - Account does not exist."
    else:
        accounts[username][placeName] = {}
        return f"Place {placeName} added to {username}'s account."


def addRoomToPlace(username, placeName, roomName):
    if username not in accounts or placeName not in accounts[username]:
        return "Error - Place does not exist in the account."
    else:
        accounts[username][placeName][roomName] = {}
        return f"Room {roomName} added to {placeName}."


def addAssetToRoom(username, placeName, roomName, assetName, price):
    if username not in accounts or placeName not in accounts[username] or roomName not in accounts[username][placeName]:
        return "Error - Can't add an asset there."
    else:
        accounts[username][placeName][roomName][assetName] = price
        return f"Asset {assetName} added to {roomName} in {placeName}."


def listAssets(username, placeName):
    if username not in accounts or placeName not in accounts[username]:
        return "Error - Place does not exist in the account."
    else:
        assetsList = ""
        for room, assets in accounts[username][placeName].items():
            for asset, price in assets.items():
                assetsList += f"{asset} in {room}: ${price}\n"
        return assetsList.strip()


def deleteAsset(username, placeName, roomName, assetName):
    try:
        del accounts[username][placeName][roomName][assetName]
        return f"Asset {assetName} deleted from {roomName} in {placeName}."
    except KeyError:
        return "Error - Asset not found."


def editAsset(username, placeName, roomName, assetName, newPrice):
    if username in accounts and placeName in accounts[username] and roomName in accounts[username][
        placeName] and assetName in accounts[username][placeName][roomName]:
        accounts[username][placeName][roomName][assetName] = newPrice
        return f"Asset {assetName} in {roomName} updated to ${newPrice}."
    else:
        return "Error - Asset not found for update."


account_name = input("Type in your name to create an account! ")
print(createAccount(account_name))

account_place = input("Type in a place (e.g., home) where assets are stored: ")
print(createPlace(account_name, account_place))

account_room = input("Type in a room in the place where assets are stored: ")
print(addRoomToPlace(account_name, account_place, account_room))

while True:
    asset = input(
        "Type the name of an asset in the room you previously added (or type 'done' to finish adding assets): ")
    if asset.lower() == 'done':
        break
    cost = float(input("Type the cost of the previously added asset: "))
    print(addAssetToRoom(account_name, account_place, account_room, asset, cost))

while True:
    print("\nOptions:")
    print("1 - Add an asset")
    print("2 - View asset list")
    print("3 - Edit an asset")
    print("4 - Delete an asset")
    print("5 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_asset = input("Type the name of the new asset: ")
        new_cost = float(input("Type the cost of the new asset: "))
        print(addAssetToRoom(account_name, account_place, account_room, new_asset, new_cost))
    elif choice == "2":
        print("\nAsset List:")
        print(listAssets(account_name, account_place))
    elif choice == "3":
        edit_room = input("Enter the room of the asset you want to edit: ")
        edit_asset = input("Enter the name of the asset you want to edit: ")
        new_price = float(input("Enter the new price of the asset: "))
        print(editAsset(account_name, account_place, edit_room, edit_asset, new_price))
    elif choice == "4":
        del_room = input("Enter the room of the asset you want to delete: ")
        del_asset = input("Enter the name of the asset you want to delete: ")
        print(deleteAsset(account_name, account_place, del_room, del_asset))
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option, please try again.")
