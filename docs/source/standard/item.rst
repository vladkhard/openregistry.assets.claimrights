.. . Kicking page rebuild 2014-10-30 17:00:08
.. include:: defs.hrst

.. index:: Item, Parameter, Classification, CAV, Unit

.. _Item:

Item
====

Schema
------

:id:
    string, auto-generated

:description:
    string, multilingual, required

    |ocdsDescription|
    A description of the goods, services to be provided.
    
    Brief description of the claim right.
    
:classification:
    :ref:`Classification`

    |ocdsDescription|
    The primary classification for the item. See the
    `itemClassificationScheme` to identify preferred classification lists,
    including CAV and GSIN.

    It is required for `classification.scheme` to be `CAV`. The
    `classification.id` should be valid CAV code.

:additionalClassifications:
    List of :ref:`Classification` objects

    |ocdsDescription|
    An array of additional classifications for the item. See the
    `itemClassificationScheme` codelist for common options to use in OCDS. 
    This may also be used to present codes from an internal classification
    scheme.

:unit:
    :ref:`Unit`

    |ocdsDescription| 
    Description of the unit which the good comes in e.g.  hours, kilograms. 
    Made up of a unit name, and the value of a single unit.

:quantity:
    decimal

    |ocdsDescription|
    The number of units required

:address:
    :ref:`Address`

    Address of location
:location:
    dictionary

    Geographical coordinates of the location. Element consists of the following items:

    :latitude:
        string, required
    :longitude:
        string, required
    :elevation:
        string, optional, usually not used

    `location` usually takes precedence over `address` if both are present.




