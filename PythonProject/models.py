# Classes of all in-game objects, importable from .csv data downloaded in da game
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

"""If you're reading this, know that I spend nearly four hours building and then rebuilding this dogshit because god 
forbid a man do something fun with his time. HOWEVER. I sincerely hope that in doing this, I have saved myself a ton 
of time down the line (which is to say, as I build the next part of this). The time is 23:36 on 18-11-2026. I will 
report back soon as to whether or not I did in fact save myself some time."""
@dataclass
class Vessel:
    name: str
    age: float
    length: float
    width: float
    draft: float
    dwt: float
    gt: float
    engine: float
    speed: float
    consumption: float
    hotel_consumption: float
    bunker_capacity: float
    draft_empty: float
    draft_tropic: float
    draft_wna: float
    ice_class: bool
    bi_fuel: bool
    cargo_volume: float
    holds: float
    opening_length: float
    opening_width: float
    floor_strength: float
    cranes: float
    maintenance: float
    insurance: float
    crew_wage: float
    administration: float
    total_opex: float
    available_in: float
    available_at: str
    time_until_docking: float
    vessel_price: float
    fuel_value: float
    spare_parts_value: float
    sundry_value: float
    broker_fee: float
    total_price: float

@dataclass
class Contract:
    start_port: Port
    start_week: float
    destination: Port
    duration: float
    weight: float
    cranes: bool
    ice_class: bool
    bi_fuel: bool
    rate: float
    currency: str
    penalty: float
    broker: Broker
    commission: float
    minimal_liking: float
    bid: float

@dataclass
class VoyageCharter(Contract):
    cargo: Cargo
    port_days: float
    sshinc: bool
    demurage: float
    signing_fee: float
    contract_type: str = "Voyage Charter"

@dataclass
class TimeCharter(Contract):
    cargo_volume: float
    floor_strength: float
    maintenance_period: float
    monthly_payment_date: float
    contract_type: str = "Time Charter"

@dataclass
class ContractOfAffreightment(Contract):
    pickup_interval: float
    cargo: Cargo
    discharge_time: float
    sshinc: bool
    demurage: float
    contract_type: str = "Contract Of Affreightment"


@dataclass
class Cargo:
    cargo_type: str
    density: float
    cargo_length: float
    cargo_width: float
    minimum_floor_strength: float
    transport_on_deck: bool


@dataclass
class Port:
    name: str
    region: str
    yearly_port_trade: float
    port_tariff: float
    bunker_price: float
    waiting_time: float
    loading_capacity: float
    unloading_capacity: float
    penalty_for_greylisted_flag: bool
    penalty_for_high_sulphur_fuel: bool
    ice_class_required: bool
    port_limit: float
    dock_size: float
    repair_costs: float


@dataclass
class Route:
    canal: bool
    canal_width: float
    canal_depth: float
    canal_fee: float
    distance_using_canal: float
    distance_not_using_canal: float
    risk_of_piracy: float
    applicable_loadline: str
    start_port: Port
    end_port: Port


@dataclass
class Broker:
    broker_name: str
    focus_country_1: Country
    focus_country_2: Country
    focus_cargo_1: Cargo
    focus_cargo_2: Cargo
    current_liking: float


@dataclass
class Country:
    region: str
    week: float
    gdp: float
    import_val: float
    export_val: float
    wage: float
    interest: float
    inflation: float  # Note: Inflation is given as an integer value, but I assume it is meant to be a percent
    exchange_rate: float


@dataclass
class Flag:
    flag: str
    flag_of_convenience: bool
    port_state_inspection_score: float
    gt_tax: float
    profit_tax: float
    revenue_tax: float

@dataclass
class OwnedContract:
    id: float
    contract_type: str
    contract: Contract
    active: bool = False
    underway: bool = False
    assigned_vessel: Optional[Vessel] = None