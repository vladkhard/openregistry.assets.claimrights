.. include:: defs.hrst

.. index:: Debt, debtValue, debtCurrencyValue

.. _debt:

Debt
======

Schema 
-------

:agreementNumber:
    string

    Number of the agreement signed.

:dateSigned:
    string

    |ocdsDescription| 
    The date the agreement was signed. In the case of multiple signatures, the date of the last signature.

:debtorType:
    string

    Possible values are naturalPerson and legalPerson.

:value:
	:ref:`debtValue`

	indebtedness, UAH

:debtCurrencyValue:
	:ref:`debtCurrencyValue`



.. _debtValue:

debtValue
=========

Schema
------

:currency:
	string

	|ocdsDescription|
	The currency in 3-letter ISO 4217 format.

	The only possible value is UAH.

:amount:
	float

	The aggregate amount of indebtedness calculated in UAH.

.. _debtCurrencyValue:

debtCurrencyValue
=================

Schema
------

:currency:
	string

	|ocdsDescription| 
	The currency in 3-letter ISO 4217 format.

	Debt currency.

:amount:
	float

	The aggregate amount of indebtedness calculated in the currency of debt.