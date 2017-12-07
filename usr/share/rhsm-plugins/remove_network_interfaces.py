import logging
import logging.handlers

from subscription_manager.base_plugin import SubManPlugin

requires_api_version = "1.0"

class FactsPlugin(SubManPlugin):
	name = 'remove_network_interfaces fact'


	def post_facts_collection_hook(self, conduit):
		keys_to_remove = []
		for key in conduit.facts:
			if "net.interface" in key:
				keys_to_remove.append(key)

		for key in keys_to_remove:
			conduit.facts.pop(key)
