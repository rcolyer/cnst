# cnst

This python package provides convenient access to constants from physics, astronomy, and mathematics.

# API examples

* `cnst.c` -- The speed of light, accessed by shortcut
* `cnst.info['G']` -- Dictionary summarizing the available info for the Newtonian constant of gravitation
* `cnst.search('moon')` -- Dictionary of information for available constants with "moon" in the name, case-insensitive.
* `cnst.all` -- Dictionary of all values available.
* `cnst['Compton wavelength'] -- Direct access for non-shortcut values by name.
* `cnst.unit['hbar'] -- A string of the unit for this constant.
* `f'{cnst.m_e} +/- {cnst.uncertainty["m_e"]} {cnst.unit["m_e"]}'` -- Produces `'9.1093837015e-31 +/- 2.8e-40 kg'`

# License

cnst is licensed under the MIT license for permissive use.

