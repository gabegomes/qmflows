__all__ = ['example_partial_geometry_opt']

from noodles import gather
from qmflows import adf, run, Settings, templates, molkit


def example_partial_geometry_opt():
    """
    Performa partial optimization freezing the Hydrogen atoms
    """
    methanol = molkit.from_smiles('CO')

    # optimize only H atoms
    s = Settings()
    s.freeze = [1, 2]
    geom_job1 = adf(templates.geometry.overlay(s), methanol, job_name='geom_job1').molecule

    # optimize only H atoms
    s = Settings()
    s.selected_atoms = ['H']
    geom_job2 = adf(templates.geometry.overlay(s), methanol, job_name='geom_job2').molecule

    geom1, geom2 = run(gather(geom_job1, geom_job2), n_processes=1)

    return geom1, geom2
