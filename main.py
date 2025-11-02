
menu = {"Pasta Primavera": 249.50, "Beef Tapa": 199.00, "Mango Cheesecake": 175.00}
tax_rate = 0.08

def calculate_total():
    item = Element("item").element.value
    qty = int(Element("quantity").element.value)
    customer = Element("customer").element.value

    subtotal = menu[item] * qty
    total = subtotal + (subtotal * tax_rate)

    summary_html = f"""
    <p><strong>Customer:</strong> {customer}</p>
    <p><strong>Item:</strong> {item} x{qty}</p>
    <p><strong>Subtotal:</strong> ₱{subtotal:.2f}</p>
    <p><strong>Tax (8%):</strong> ₱{subtotal*tax_rate:.2f}</p>
    <p><strong>Total:</strong> ₱{total:.2f}</p>
    """

    Element("summary").element.innerHTML = summary_html
