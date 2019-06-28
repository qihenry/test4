from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

# Front-end
SERVER_PATH = ROOT_PATH / 'server'

COMS_PATH = ROOT_PATH / 'coms'
# Recon
RECON_PATH = ROOT_PATH / 'server' / 'recon'
RECON_ASSETS_PATH = RECON_PATH / 'drunck' / 'assets'

# Quant
SERVER_ANALYZE_PATH = COMS_PATH / 'server' / 'ana'

# GT
SERVER_SIM_BLOCH_PATH = SERVER_PATH / 'simulation' / 'bloch'
SERVER_SIM_OUTPUTS_PATH = SERVER_PATH / 'simulation' / 'outputs'
SERVER_RX_PATH = SERVER_PATH / 'rx'
COMS_RX_OUTPUTS_PATH = COMS_PATH / 'coms_ui' / 'static' / 'Rx' / 'outputs'
COMS_RX_INPUTS_PATH = COMS_PATH / 'coms_ui' / 'static' / 'Rx' / 'inputs'
COMS_SIM_OUTPUTS_PATH = COMS_PATH / 'coms_ui' / 'static' / 'acq' / 'outputs'

STATIC_ANALYZE_PATH = Path('static') / 'ana'
STATIC_ACQUIRE_PATH = Path('static') / 'acq'
STATIC_RF_PATH = Path('static') / 'rf'
STATIC_RX_PATH = Path('static') / 'Rx' / 'outputs'
STATIC_RECON_PATH = Path('static') / 'Recon'
USER_UPLOAD_FOLDER = ROOT_PATH / 'coms' / 'coms_ui' / 'static' / 'user_uploads'
