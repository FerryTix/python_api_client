# coding: utf-8

# flake8: noqa

"""
    FerryTix

    This is the api for the FerryTix Passenger Ferry Ticketing System, that is both accessible to the vending machines and to other clients.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hendrik.lankers.hl@googlemail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.default_api import DefaultApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.bank_transfer_payment import BankTransferPayment
from swagger_client.models.cash_payment import CashPayment
from swagger_client.models.ec_card_payment import ECCardPayment
from swagger_client.models.faehr_card import FaehrCard
from swagger_client.models.faehr_card_payment import FaehrCardPayment
from swagger_client.models.fare import Fare
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response201 import InlineResponse201
from swagger_client.models.machine_command import MachineCommand
from swagger_client.models.machine_configuration import MachineConfiguration
from swagger_client.models.machine_location import MachineLocation
from swagger_client.models.machine_status import MachineStatus
from swagger_client.models.machine_status_tickets_sold_today import MachineStatusTicketsSoldToday
from swagger_client.models.one_of_machine_command import OneOfMachineCommand
from swagger_client.models.pay_pal_payment import PayPalPayment
from swagger_client.models.payment import Payment
from swagger_client.models.position import Position
from swagger_client.models.refill_paper_roll_command import RefillPaperRollCommand
from swagger_client.models.staff_member import StaffMember
from swagger_client.models.staff_role import StaffRole
from swagger_client.models.ticket_class import TicketClass
from swagger_client.models.ticket_sale import TicketSale
from swagger_client.models.top_up import TopUp
from swagger_client.models.vending_machine import VendingMachine
from swagger_client.models.waiting_passenger import WaitingPassenger
