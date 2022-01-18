from tkinter import *
from datetime import datetime
from bs4 import BeautifulSoup
from urllib import request
import urllib


root = Tk()
root.title('Ethereum Price Tracker')
root.iconbitmap('file:///Users/orhanbenli/Desktop/py/t.ico')
root.geometry("600x425")
root.config(bg="#215CAF")

global prev
prev = False

# Let's get current time
r_now = datetime.now()
c_time = r_now.strftime("%I:%M:%S %p")

# Let's create an ETH Frame
eth_frame = Frame(root, bg="white")
eth_frame.pack(pady=18)

# Let's define ETH Logo Image
eth_logo = PhotoImage(file='eth.gif')
eth_logo_label = Label(eth_frame, image=eth_logo, bd=1)
eth_logo_label.grid(row=0, column=0, rowspan=2)

# Let's add ETH Price Label
eth_label = Label(eth_frame, text='ethtest', 
	font=("Georgia", 50),
	bg="white",
	fg="black",
	bd=0)
eth_label.grid(row=0, column=1, padx=18, sticky="s")

# Let's find the latest ETH Price
latest_eth_price = Label(eth_frame, text="eth price test",
	font=("Georgia", 13),
	bg="white",
	fg="grey")
latest_eth_price.grid(row=1, column=1, sticky="n")

# Let's track the ETH Price
def eth_update():
	global prev

	# Tracking ETH Price
	w_page = urllib.request.urlopen("https://coinmarketcap.com/currencies/ethereum/").read()
	w_html = BeautifulSoup(w_page, "html.parser")
	eth_price = w_html.find(class_="priceValue")
	
	# Let's convert it to string in order to have slices
	eth_price1 = str(eth_price)
	# Now, getting the slice containing the price
	eth_price2 = eth_price1[31:39]

	# Let's update ETH label
	eth_label.config(text=f'${eth_price2}')
	# Setting timer (60 seconds)
	root.after(60000, eth_update)

	# Let's get current time
	r_now = datetime.now()
	c_time = r_now.strftime("%I:%M:%S %p")

	# Let's update our Status Bar
	stat_bar.config(text=f'Last Updated: {c_time}   ')

	# Let's find ETH Price Change
	# Getting current price
	eth_cur = eth_price2

	# We need to remove the comma in ETH Price
	eth_cur = eth_cur.replace(',', '')

	if prev:
		if float(prev) > float(eth_cur):
			latest_eth_price.config(
				text=f'ETH Price Down {round(float(prev)-float(eth_cur), 2)}', fg="red")

		elif float(prev) == float(eth_cur):
			latest_eth_price.config(text="ETH Price Remains The Same", fg="#696969")	

		else:
			latest_eth_price.config(
				text=f'ETH Price Up {round(float(eth_cur)-float(prev), 2)}', fg="green")			

	else:
		prev = eth_cur
		latest_eth_price.config(text="ETH Price Remains The Same", fg="grey")

# Let's create our Status Bar
stat_bar = Label(root, text=f'Last Updated {c_time}   ',
	bd=1,
	anchor=E,
	bg="white",
	fg="black")

stat_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Start and run eth_update func.
eth_update()
root.mainloop()