from nose.plugins.attrib import attr
from qmflows.examples import (
    example_generic_constraints, example_H2O2_TS, example_partial_geometry_opt)
import numpy as np


@attr('slow')
def test_partial_geometry_opt():
    """
    Test partial geometry optimization.
    """
    geom1, geom2 = example_partial_geometry_opt()
    assert str(geom1) == str(geom2)


@attr('slow')
def test_h2o2_ts():
    """
    Test TS optimization of a rotational barrier in hydrogen peroxide
    with ORCA using init hessian from DFTB.
    """
    ts_dihe, n_optcycles = example_H2O2_TS()
    assert (n_optcycles < 7)
    assert ts_dihe == 0.0


@attr('slow')
def test_generic_constraints():
    """
    Test generic distance constraints on all packages
    """
    test_energies = example_generic_constraints()[1]
    expected_energies = [
        -4.76019173, -0.28400262, -99.43865603, -4.74740691,
        -0.27647907, -99.43097285, -4.73227438, -0.25874316,
        -99.41561528]

    assert np.allclose(test_energies, expected_energies, rtol=1e-3)
