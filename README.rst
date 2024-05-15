Many2Many Relationship Between Res Partner and Sale Order
==========================================================

Description
-----------

This module enhances the functionality of Odoo by establishing a many-to-many relationship between the *res.partner* and *sale.order* models. It allows users to associate multiple partners with a single sale order and vice versa. When a value is selected in either the *res.partner* or *sale.order* fields, the current record is automatically added to the selected record.

Installation
------------

1. Download the module from the repository.
2. Add the module to your Odoo addons directory.
3. Install the module from the Odoo Apps menu.
4. Restart the Odoo server if necessary.

Usage
-----

1. Navigate to the Contacts module and open a partner/contact record.
2. Find the "Sale Orders" field, which is a many-to-many field.
3. Select one or more sale orders associated with the partner.
4. Navigate to the Sales module and open a sale order record.
5. Find the "Partners" field, which is a many-to-many field.
6. Select one or more partners associated with the sale order.

Notes
-----

- This module simplifies the management of relationships between partners and sale orders, allowing for more flexibility and efficiency in organizing data.
- The bidirectional many-to-many relationship ensures that relevant records are linked and accessible from both the partner and sale order views.
- Users can easily navigate between related records, improving overall usability and productivity.

Contributing
------------

Contributions to this module are welcome. Please submit any bug reports, feature requests, or pull requests to the repository.

License
-------

This module is licensed under the GPL-3 license. See the LICENSE file for more details.
