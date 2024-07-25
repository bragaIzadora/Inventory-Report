from inventory_report.product import Product


def test_create_product():
    product_id = "12345"
    product_name = "Notebook"
    company_name = "Tech Corp"
    manufacturing_date = "2024-01-01"
    expiration_date = "2026-01-01"
    serial_number = "ABC123XYZ"
    storage_instructions = "Store in a cool, dry place."

    product = Product(
        id=product_id,
        product_name=product_name,
        company_name=company_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions,
    )

    assert product.id == product_id
    assert product.product_name == product_name
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions
