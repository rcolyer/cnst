# cnst

This python package provides convenient access to constants from physics, astronomy, and mathematics.

# API examples

* `from cnst import cnst` -- Recommended import.
* `cnst.c` -- The speed of light, accessed by shortcut.
* `cnst.info['G']` -- Dictionary summarizing the available info for the Newtonian constant of gravitation.
* `cnst.search('moon')` -- Dictionary of information for available constants with "moon" in the name, case-insensitive.
* `print('\n'.join(cnst.search('planck').keys()))` -- Print the names of all the constants with Planck in the name.
* `cnst.label['z95']` -- Reveals the label for a constant:
  - `'mathematical / z score for 95% confidence interval'`
* `cnst.all` -- Dictionary of all values available.
* `cnst['Planck temperature']` -- Direct access for non-shortcut values by name.
* `cnst.unit['hbar']` -- A string of the unit for this constant.
* `cnst.uncertainty['Compton wavelength']` -- The absolute uncertainty of the Compton wavelength.
* `cnst.reluncert['m_Sun']` -- The relative uncertainty of the mass of the Sun.
* `cnst.table` -- The dictionary structure loaded from the json file with all of the data.
* `', '.join(cnst.table['shortcuts'].keys())` -- Show all the available shortcuts.
* `f'{cnst.m_e} \u00b1 {cnst.uncertainty["m_e"]} {cnst.unit["m_e"]}'` -- Describes the mass of the electron as:
  - `'9.1093837015e-31 ± 2.8e-40 kg'`
* `F = cnst.G*cnst.m_Earth*cnst.m_Moon/cnst.orb_Moon**2` -- Computes the gravitational force between the Earth and the Moon.
* `', '.join(f"{(1 + cnst.m_e/cnst.m_p)/(cnst.Rinf*(1-1/n**2))*1e9:.2f}nm" for n in range(2,12))` -- Generates the Lyman series of Hydrogen spectra as:
  - `'121.57nm, 102.57nm, 97.25nm, 94.98nm, 93.78nm, 93.08nm, 92.62nm, 92.32nm, 92.10nm, 91.94nm'`

# License

cnst is licensed under the MIT license for permissive use.

