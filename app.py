import tkinter as tk
from tkinter import ttk, messagebox
from core.client import create_client
from core.orders import place_order
from core.utils import get_order_types
from core.logging_config import setup_logger

client = create_client()

logger = setup_logger()
logger.info("Binance Futures Bot Started")

root = tk.Tk()
root.title("Binance Futures Trading Bot")
root.geometry("500x500")
root.resizable(False, False)

# State variables
symbol_var = tk.StringVar()
side_var = tk.StringVar(value="BUY")
order_type_var = tk.StringVar(value="MARKET")
quantity_var = tk.StringVar()
price_var = tk.StringVar()
stop_price_var = tk.StringVar()

# UI containers
form_widgets = {}
form_frame = tk.Frame(root)
form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Clear and rebuild form
def clear_form():
    for widget in form_widgets.values():
        widget.destroy()
    form_widgets.clear()

def render_form():
    clear_form()

    row = 0
    def add_field(label, var, options=None):
        nonlocal row
        tk.Label(form_frame, text=label).grid(row=row, column=0, sticky="w", padx=10, pady=5)

        if options:
            entry = ttk.Combobox(form_frame, textvariable=var, values=options, state="readonly")
            if label == "Order Type:":
                entry.bind("<<ComboboxSelected>>", lambda e: render_form())  # re-render on change
        else:
            entry = tk.Entry(form_frame, textvariable=var)

        entry.grid(row=row, column=1, padx=10, pady=5)
        form_widgets[label] = entry
        row += 1

    add_field("Symbol (e.g., BTCUSDT):", symbol_var)
    add_field("Side:", side_var, ["BUY", "SELL"])
    add_field("Order Type:", order_type_var, get_order_types())
    add_field("Quantity:", quantity_var)

    current_type = order_type_var.get().upper()
    if current_type in ["LIMIT", "STOP", "TAKE_PROFIT", "OCO"]:
        add_field("Price:", price_var)
    if current_type in ["STOP_MARKET", "STOP", "TAKE_PROFIT", "OCO"]:
        add_field("Stop Price:", stop_price_var)

    submit_btn.grid(row=row, columnspan=2, pady=20)

def submit_order():
    try:
        symbol = symbol_var.get().strip().upper()
        side = side_var.get().strip().upper()
        order_type = order_type_var.get().strip().upper()
        quantity = float(quantity_var.get())

        price = float(price_var.get()) if price_var.get() else None
        stop_price = float(stop_price_var.get()) if stop_price_var.get() else None

        result = place_order(client, symbol, side, order_type, quantity, price, stop_price)

        if "error" in result:
            messagebox.showerror("Order Failed", result["error"])
        else:
            messagebox.showinfo("Order Success", str(result))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for quantity/price.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

submit_btn = tk.Button(
    button_frame,
    text="Submit Order",
    width=20,
    height=2,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    command=submit_order
)

render_form()
root.mainloop()
