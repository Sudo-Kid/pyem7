=====
pyem7
=====

This project was started out of the need for an easier way to comunicate with ScienceLogic's
monitoring software.

The goal of this project is to build out an easy to use Python based library to interacte with
a ScienceLogic API server. I will be attempting to replicate everything in the feature list below.

Dependencies:
  - `Requests <https://pypi.python.org/pypi/requests>`_
  - `Requests Mock <https://pypi.python.org/pypi/requests-mock>`_
  - `Nose <https://pypi.python.org/pypi/nose/1.3.7>`_
  - `Tox <https://pypi.python.org/pypi/tox>`_

.. Warning::
  This project is in no way assosiated with ScienceLogic!

.. Warning::
  This has not yet been completed and should not be used in production!

**Please note that not all items in the feature list have been implemented yet.**

Feature List:
  - Accounts

    + View/search/filter the list of user accounts.
    + Create a new user account.
    + View the properties of a user account.
    + Update the properties of a user account.
    + Replace a user account.
    + Delete a user account.
    + View the list of access hooks that have been granted to a user account.

  - Alerts

    + Create a new API alert.
    + View/search/filter the list of pending API alerts.
    + View details about a pending API alert.
    + Update a pending API alert.

  - Appliances

    + View/search/filter the list of ScienceLogic appliances.
    + View the properties of a ScienceLogic appliance.
    + Update the description or IP address of a ScienceLogic appliance.

  - Assets

    + View/search/filter the list of asset records.
    + Create a new asset record.
    + View the general properties of an asset record.
    + Replace an asset record.
    + Update the general properties of an asset record.
    + Delete an asset record.
    + View/search/filter the list of components associated with an asset record.
    + Add a new component to an asset record.
    + View the properties of a component associated with an asset record.
    + Update the properties of a component associated with an asset record.
    + Replace a component associated with an asset record.
    + Delete a component from an asset record.
    + View the configuration properties of an asset /asset/X/configuration/ record.
    + Update the configuration properties of an asset record.
    + Replace the configuration properties of an asset record.
    + View/search/filter the list of software licenses associated with an asset record.
    + Add a new software license to an asset record.
    + View the properties of a software license associated with an asset record.
    + Update the properties of a software license associated with an asset record.
    + Replace a software license associated with an asset record.
    + Delete a software license from an asset record.
    + View the maintenance and service properties of an asset record.
    + Update the maintenance and service properties of an asset record.
    + Replace the maintenance and service properties of an asset record.
    + View/search/filter the list of IP networks associated with an asset record.
    + Add a new IP network to an asset record.
    + View the properties of an IP network associated with an asset record.
    + Update the properties of an IP network associated with an asset record.
    + Replace an IP network associated with an asset record.
    + Delete an IP network from an asset record.

  - Collector Groups
    
    + View/search/filter the list of collector groups.
    + Create a new collector group.
    + View the properties of a collector group.
    + Update the properties of a collector group.
    + Replace a collector group.
    + Delete a collector group.

  - Credentials

    + View the index of available credential resources.
    + View/search/filter the list of basic/snippet credentials.
    + Create a new basic/snippet credential.
    + View a basic/snippet credential.
    + Update a basic/snippet credential.
    + Replace a basic/snippet credential.
    + Delete a basic/snippet credential.
    + View/search/filter the list of database credentials.
    + Create a new database credential.
    + View a database credential.
    + Update a database credential.
    + Replace a database credential.
    + Delete a database credential.
    + View/search/filter the list of LDAP/AD credentials.
    + Create a new LDAP/AD credential.
    + View a LDAP/AD credential.
    + Update a LDAP/AD credential.
    + Replace a LDAP/AD credential.
    + Delete a LDAP/AD credential.
    + View/search/filter the list of PowerShell credentials.
    + Create a new PowerShell credential.
    + View a PowerShell credential.
    + Update a PowerShell credential.
    + Replace a PowerShell credential.
    + Delete a PowerShell credential.
    + View/search/filter the list of SNMP credentials.
    + Create a new SNMP credential.
    + View an SNMP credential.
    + Update an SNMP credential.
    + Replace an SNMP credential.
    + Delete an SNMP credential.
    + View/search/filter the list of SOAP/XML credentials.
    + Create a new SOAP/XML credential.
    + View a SOAP/XML credential.
    + Update a SOAP/XML credential.
    + Replace a SOAP/XML credential.
    + Delete a SOAP/XML credential.
    + View/search/filter the list of SSH credentials.
    + Create a new SSH credential.
    + View an SSH credential.
    + Update an SSH credential.
    + Replace an SSH credential.
    + Delete an SSH credential.

  - Custom Attributes

    + View the index of available custom attribute resources.
    + Update the custom attributes defined for assets.
    + View the custom attributes defined for assets.
    + Update the custom attributes defined for devices.
    + View the custom attributes defined for devices.
    + Update the custom attributes defined for themes.
    + View the custom attributes defined for themes.
    + Update the custom attributes defined for vendors.
    + View the custom attributes defined for vendors.

  - Dashboards

    + View/search/filter the list of dashboards.
    + Create a new dashboard.
    + View the properties of a dashboard.
    + Update the properties of a dashboard.
    + Replace a dashboard.
    + Delete a dashboard.
    + View/search/filter the list of widgets on a dashboard.
    + View the properties of a widget on a dashboard.
    + Update the properties of a widget on a dashboard.
    + Replace a widget on a dashboard.
    + Remove a widget from a dashboard.
    + Create a new dashboard by duplicating an existing dashboard.

  - Devices

    + View/search/filter the list of devices.
    + Create a new virtual device.
    + View the properties of a device.
    + Update the properties of a device.
    + Replace the properties of a device.
    + Delete a device.
    + View/search/filter the list of Dynamic Applications aligned with a device.
    + Align a Dynamic Application with a device.
    + View the collection status and associated credential for a Dynamic Application aligned with a device.
    + Update the collection status and associated credential for a Dynamic Application aligned with a device.
    + Unalign a Dynamic Application from a device.
    + View/search/filter the list of available configuration data for a device.
    + View meta-data about data collected from a device by a configuration Dynamic Application.
    + View data collected from a device by a configuration Dynamic Application.
    + View historical snapshots of data collected from a device by a configuration Dynamic Application.
    + View general information collected from a device.
    + View/search/filter the list of credentials aligned with a device.
    + View the threshold settings for a device.
    + Update the threshold settings for a device.
    + Replace the threshold settings for a device.
    + Revert all device thresholds to the global default values.
    + View/search/filter the list of interfaces for a device.
    + View the properties of an interface for a device.
    + Update the properties of an interface for a device.
    + View data for an interface.
    + View daily normalized data for an interface.
    + View hourly normalized data for an interface.
    + View/search/filter the list of logs associated with a device.
    + View a log associated with a device.
    + Add a note to a device.
    + View/search/filter the list of notes associated with a device. 
    + View a note associated with a device.
    + Update a note associated with a device.
    + Replace a note associated with a device.
    + Delete a note associated with a device.
    + View/search/filter the list of available Dynamic Application data for a device.
    + View data for a Dynamic Application aligned to a device.
    + View daily normalized data for a Dynamic Application aligned to a device.
    + View hourly normalized data for a Dynamic Application aligned to a device.
    + View/search/filter the list of available vitals data for a device.
    + View availability data for a device.
    + View daily normalized availability data for a device.
    + View hourly normalized availability data for a device.
    + View data for a file system on a device.
    + View daily normalized data for a file system on a device.
    + View latency data for a device.
    + View daily normalized latency data for a device.
    + View hourly normalized latency data for a device.
    + Apply a device template to a device.

  - Device Categories

    + View/search/filter the list of device categories.
    + View the properties of a device category.

  - Device Classes

    + View/search/filter the list of device classes.
    + View the properties of a device class.

  - Device Groups

    + View/search/filter the list of device groups.
    + Create a new device group.
    + View the properties of a device group.
    + Update the properties of a device group.
    + Replace a device group.
    + Delete a device group.
    + View a list of all devices in the device group, including devices that match dynamic rules.
    + Apply a device template to a device group.

  - Device Templates

    + View/search/filter the list of device templates.
    + Create a new device template.
    + View the properties of a device template.
    + Update the properties of a device template.
    + Replace a device template.
    + Delete a device template.
    + View/search/filter the list of web content monitoring policy sub-templates associated with a device template.
    + Create a new web content monitoring policy sub-template for a device template.
    + View the properties of a web content monitoring policy sub-template associated with a device template.
    + Update a web content monitoring policy sub-template associated with a device template.
    + Replace a web content monitoring policy sub-template associated with a device template.
    + Delete a web content monitoring policy sub-template associated with a device template.
    + View/search/filter the list of Dynamic Application sub-templates associated with a device template.
    + Create a new Dynamic Application sub-template for a device template.
    + View the properties of a Dynamic Application sub-template associated with a device template.
    + Update a Dynamic Application sub-template associated with a device template.
    + Replace a Dynamic Application sub-template associated with a device template.
    + Delete a Dynamic Application sub-template associated with a device template.
    + View/search/filter the list of port monitoring policy sub-templates associated with a device template.
    + Replace a Windows service monitoring policy sub-template associated with a device template.
    + Delete a Windows service monitoring policy sub-template associated with a device template.

  - Discovery Sessions

    + View/search/filter the list of discovery sessions.
    + Create a new discovery session.
    + View the properties of a discovery session.
    + Update a discovery session.
    + Replace a discovery session.
    + Delete a discovery session.
    + View/search/filter the list of logs associated with a discovery session.
    + View a log message associated with a discovery session.
    + View/search/filter the list of currently running discovery sessions.
    + Create and immediately run a new discovery session.
    + View the properties of a currently running discovery session.
    + Stop a currently running discovery session.
    + View/search/filter the list of logs associated with a currently running discovery session.
    + View a log message associated with a currently running discovery session.
    + Start a discovery session.

  - Dynamic Applications

    + View the index of available Dynamic Application resources.
    + View/search/filter the list of Database Configuration Dynamic Applications.
    + View the properties of a Database Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with a Database Configuration Dynamic Application.
    + Add a collection object to a Database Configuration Dynamic Application.
    + View the properties of a collection object associated with a Database Configuration Dynamic Application.
    + Update the properties of a collection object associated with a Database Configuration Dynamic Application.
    + Replace a collection object associated with a Database Configuration Dynamic Application.
    + Remove a collection object from a Database Configuration Dynamic Application.
    + View/search/filter the list of Database Performance Dynamic Applications.
    + View the properties of a Database Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with a Database Performance Dynamic Application.
    + Add a collection object to a Database Performance Dynamic Application.
    + View the properties of a collection object associated with a Database Performance Dynamic Application.
    + Update the properties of a collection object associated with a Database Performance Dynamic Application.
    + Replace a collection object associated with a Database Performance Dynamic Application.
    + Remove a collection object from a Database Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with a Database Performance Dynamic Application.
    + Add a presentation object to a Database Performance Dynamic Application.
    + View the properties of a presentation object associated with a Database Performance Dynamic Application.
    + Update the properties of a presentation object associated with a Database Performance Dynamic Application.
    + Replace a presentation object associated with a Database Performance Dynamic Application.
    + Remove a presentation object from a Database Performance Dynamic Application.
    + View/search/filter the list of PowerShell Configuration Dynamic Applications.
    + View the properties of a PowerShell Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with a PowerShell Configuration Dynamic Application.
    + Add a collection object to a PowerShell Configuration Dynamic Application.
    + View the properties of a collection object associated with a PowerShell Configuration Dynamic Application.
    + Update the properties of a collection object associated with a PowerShell Configuration Dynamic Application.
    + Replace a collection object associated with a PowerShell Configuration Dynamic Application.
    + Remove a collection object from a PowerShell Configuration Dynamic Application.
    + View/search/filter the list of PowerShell Performance Dynamic Applications.
    + View the properties of a PowerShell Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with a PowerShell Performance Dynamic Application.
    + Add a collection object to a PowerShell Performance Dynamic Application.
    + View the properties of a collection object associated with a PowerShell Performance Dynamic Application.
    + Update the properties of a collection object associated with a PowerShell Performance Dynamic Application.
    + Replace a collection object associated with a PowerShell Performance Dynamic Application.
    + Remove a collection object from a PowerShell Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with a PowerShell Performance Dynamic Application.
    + Add a presentation object to a PowerShell Performance Dynamic Application.
    + View the properties of a presentation object associated with a PowerShell Performance Dynamic Application.
    + Update the properties of a presentation object associated with a PowerShell Performance Dynamic Application.
    + Replace a presentation object associated with a PowerShell Performance Dynamic Application.
    + Remove a presentation object from a PowerShell Performance Dynamic Application.
    + View/search/filter the list of Snippet Configuration Dynamic Applications.
    + View the properties of a Snippet Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with a Snippet Configuration Dynamic Application.
    + Add a collection object to a Snippet Configuration Dynamic Application.
    + View the properties of a collection object associated with a Snippet Configuration Dynamic Application.
    + Update the properties of a collection object associated with a Snippet Configuration Dynamic Application.
    + Replace a collection object associated with a Snippet Configuration Dynamic Application.
    + Remove a collection object from a Snippet Configuration Dynamic Application.
    + View/search/filter the list of Snippet Journal Dynamic Applications.
    + View the properties of a Snippet Journal Dynamic Application.
    + View/search/filter the list of collection objects associated with a Snippet Journal Dynamic Application.
    + Add a collection object to a Snippet Journal Dynamic Application.
    + View the properties of a collection object associated with a Snippet Journal Dynamic Application.
    + Update the properties of a collection object associated with a Snippet Journal Dynamic Application.
    + Replace a collection object associated with a Snippet Journal Dynamic Application.
    + Remove a collection object from a Snippet Journal Dynamic Application.
    + Add a presentation object to a Snippet Journal Dynamic Application.
    + View/search/filter the list of presentation objects associated with a Snippet Journal Dynamic Application.
    + View the properties of a presentation object associated with a Snippet Journal Dynamic Application.
    + Update the properties of a presentation object associated with a Snippet Journal Dynamic Application.
    + Replace a presentation object associated with a Snippet Journal Dynamic Application.
    + Remove a presentation object from a Snippet Journal Dynamic Application.
    + View/search/filter the list of Snippet Performance Dynamic Applications.
    + View the properties of a Snippet Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with a Snippet Performance Dynamic Application.
    + Add a collection object to a Snippet Performance Dynamic Application.
    + View the properties of a collection object associated with a Snippet Performance Dynamic Application.
    + Update the properties of a collection object associated with a Snippet Performance Dynamic Application.
    + Replace a collection object associated with a Snippet Performance Dynamic Application.
    + Remove a collection object from a Snippet Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with a Snippet Performance Dynamic Application.
    + Add a presentation object to a Snippet Performance Dynamic Application.
    + View the properties of a presentation object associated with a Snippet Performance Dynamic Application.
    + Update the properties of a presentation object associated with a Snippet Performance Dynamic Application.
    + Replace a presentation object associated with a Snippet Performance Dynamic Application.
    + Remove a presentation object from a Snippet Performance Dynamic Application.
    + View/search/filter the list of SNMP Configuration Dynamic Applications.
    + View the properties of an SNMP Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with an SNMP Configuration Dynamic Application.
    + Add a collection object to an SNMP Configuration Dynamic Application.
    + View the properties of a collection object associated with an SNMP Configuration Dynamic Application.
    + Update the properties of a collection object associated with an SNMP Configuration Dynamic Application.
    + Replace a collection object associated with an SNMP Configuration Dynamic Application.
    + Remove a collection object from an SNMP Configuration Dynamic Application.
    + View/search/filter the list of SNMP Performance Dynamic Applications.
    + View the properties of an SNMP Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with an SNMP Performance Dynamic Application.
    + Add a collection object to an SNMP Performance Dynamic Application.
    + View the properties of a collection object associated with an SNMP Performance Dynamic Application.
    + Update the properties of a collection object associated with an SNMP Performance Dynamic Application.
    + Replace a collection object associated with an SNMP Performance Dynamic Application.
    + Remove a collection object from an SNMP Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with an SNMP Performance Dynamic Application.
    + Add a presentation object to an SNMP Performance Dynamic Application.
    + View the properties of a presentation object associated with an SNMP Performance Dynamic Application.
    + Update the properties of a presentation object associated with an SNMP Performance Dynamic Application.
    + Replace a presentation object associated with an SNMP Performance Dynamic Application.
    + Remove a presentation object from an SNMP Performance Dynamic Application.
    + View/search/filter the list of SOAP Configuration Dynamic Applications.
    + View the properties of a SOAP Configuration Dynamic Application.
    + Add a collection object to a SOAP Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with a SOAP Configuration Dynamic Application.
    + View the properties of a collection object associated with a SOAP Configuration Dynamic Application.
    + Update the properties of a collection object associated with a SOAP Configuration Dynamic Application.
    + Replace a collection object associated with a SOAP Configuration Dynamic Application.
    + Remove a collection object from a SOAP Configuration Dynamic Application.
    + View/search/filter the list of SOAP Performance Dynamic Applications.
    + View the properties of a SOAP Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with a SOAP Performance Dynamic Application.
    + Add a collection object to a SOAP Performance Dynamic Application.
    + View the properties of a collection object associated with a SOAP Performance Dynamic Application.
    + Update the properties of a collection object associated with a SOAP Performance Dynamic Application.
    + Replace a collection object associated with a SOAP Performance Dynamic Application..
    + Remove a collection object from a SOAP Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with a SOAP Performance Dynamic Application.
    + Add a presentation object to a SOAP Performance Dynamic Application.
    + View the properties of a presentation object associated with a SOAP Performance Dynamic Application.
    + Update the properties of a presentation object associated with a SOAP Performance Dynamic Application.
    + Replace a presentation object associated with a SOAP Performance Dynamic Application.
    + Remove a presentation object from a SOAP Performance Dynamic Application.
    + View/search/filter the list of WMI Configuration Dynamic Applications.
    + View the properties of a WMI Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with a WMI Configuration Dynamic Application.
    + Add a collection object to a WMI Configuration Dynamic Application.
    + View the properties of a collection object associated with a WMI Configuration Dynamic Application.
    + Update the properties of a collection object associated with a WMI ConfigurationDynamic Application.
    + Replace a collection object associated with a WMI Configuration Dynamic Application.
    + Remove a collection object from a WMI Configuration Dynamic Application.
    + View/search/filter the list of WMI Performance Dynamic Applications.
    + View the properties of a WMI Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with a WMI Performance Dynamic Application.
    + Add a collection object to a WMI Performance Dynamic Application.
    + View the properties of a collection object associated with a WMI Performance Dynamic Application.
    + Update the properties of a collection object associated with a WMI Performance Dynamic Application.
    + Replace a collection object associated with a WMI Performance Dynamic Application.
    + Remove a collection object from a WMI Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with a WMI Performance Dynamic Application.
    + Add a presentation object to a WMI Performance Dynamic Application.
    + View the properties of a presentation object associated with a WMI Performance Dynamic Application.
    + Update the properties of a presentation object associated with a WMI Performance Dynamic Application.
    + Replace a presentation object associated with a WMI Performance Dynamic Application.
    + Remove a presentation object from a WMI Performance Dynamic Application.
    + View/search/filter the list of XML Configuration Dynamic Applications.
    + View the properties of an XML Configuration Dynamic Application.
    + Add a collection object to an XML Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with an XML Configuration Dynamic Application.
    + View the properties of a collection object associated with an XML Configuration Dynamic Application.
    + Update the properties of a collection object associated with an XML Configuration Dynamic Application.
    + Replace a collection object associated with an XML Configuration Dynamic Application.
    + Remove a collection object from an XML Configuration Dynamic Application.
    + View/search/filter the list of XML Performance Dynamic Applications.
    + View the properties of an XML Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with an XML Performance Dynamic Application.
    + Add a collection object to an XML Performance Dynamic Application.
    + View the properties of a collection object associated with an XML Performance Dynamic Application.
    + Update the properties of a collection object associated with an XML Performance Dynamic Application.
    + Replace a collection object associated with an XML Performance Dynamic Application.
    + Remove a collection object from an XML Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with an XML Performance Dynamic Application.
    + Add a presentation object to an XML Performance Dynamic Application.
    + View the properties of a presentation object associated with an XML Performance Dynamic Application.
    + Update the properties of a presentation object associated with an XML Performance Dynamic Application.
    + Replace a presentation object associated with an XML Performance Dynamic Application.
    + Remove a presentation object from an XML Performance Dynamic Application.
    + View/search/filter the list of XSLT Configuration Dynamic Applications.
    + View the properties of an XSLT Configuration Dynamic Application.
    + View/search/filter the list of collection objects associated with an XSLT Configuration Dynamic Application.
    + Add a collection object to an XSLT Configuration Dynamic Application.
    + View the properties of a collection object associated with an XSLT Configuration Dynamic Application.
    + Update the properties of a collection object associated with an XSLT Configuration Dynamic Application.
    + Replace a collection object associated with a Dynamic Application.
    + Remove a collection object from an XSLT Configuration Dynamic Application.
    + View/search/filter the list of XSLT Performance Dynamic Applications.
    + View the properties of an XSLT Performance Dynamic Application.
    + View/search/filter the list of collection objects associated with an XSLT Performance Dynamic Application.
    + Add a collection object to an XSLT Performance Dynamic Application.
    + View the properties of a collection object associated with an XSLT Performance Dynamic Application.
    + Update the properties of a collection object associated with an XSLT Performance Dynamic Application.
    + Replace a collection object associated with an XSLT Performance Dynamic Application.
    + Remove a collection object from an XSLT Performance Dynamic Application.
    + View/search/filter the list of presentation objects associated with an XSLT Performance Dynamic Application.
    + Add a presentation object to an XSLT Performance Dynamic Application.
    + View the properties of a presentation object associated with an XSLT Performance Dynamic Application.
    + Update the properties of a presentation object associated with an XSLT Performance Dynamic Application.
    + Replace a presentation object associated with an XSLT Performance Dynamic Application.
    + Remove a presentation object from an XSLT Performance Dynamic Application.
    + View/search/filter the list of all Dynamic Applications.

  - Events

    + View/search/filter the list of active events.
    + View an active event.
    + Clear an active event.
    + Update the properties of an event.

  - External Contacts

    + View/search/filter the list of external contacts.
    + Create a new external contact.
    + View the properties of an external contact.
    + Update the properties of an external contact.
    + Replace an external contact.
    + Delete an external contact.

  - Monitors

    + View the index of available monitoring policy resources.
    + View/search/filter the list of web content monitoring policies.
    + Create a new web content monitoring policy.
    + View a web content monitoring policy.
    + Update a web content monitoring policy.
    + Replace a web content monitoring policy.
    + Delete a web content monitoring policy.
    + View/search/filter the list of domain name monitoring policies.
    + Create a new domain name monitoring policy.
    + View a domain name monitoring policy.
    + Update a domain name monitoring policy.
    + Replace a domain name monitoring policy.
    + Delete a domain name monitoring policy.
    + View/search/filter the list of Email round-trip monitoring policies.
    + Create a new Email round-trip monitoring policy.
    + View an Email round-trip monitoring policy.
    + Update an Email round-trip monitoring policy.
    + Replace an Email round-trip monitoring policy.
    + Delete an Email round-trip monitoring policy.
    + View/search/filter the list of port monitoring policies.
    + Create a new port monitoring policy.
    + View a port monitoring policy.
    + Update a port monitoring policy.
    + Replace a port monitoring policy.
    + Delete a port monitoring policy.
    + Create a new system process monitoring policy.
    + View/search/filter the list of system process monitoring policies.
    + View a system process monitoring policy.
    + Update a system process monitoring policy.
    + Replace a system process monitoring policy.
    + Delete a system process monitoring policy.
    + View/search/filter the list of Windows service monitoring policies.
    + Create a new Windows service monitoring policy.
    + View a Windows service monitoring policy.
    + Update a Windows service monitoring policy.
    + Replace a Windows service monitoring policy.
    + Delete a Windows service monitoring policy.
    + View/search/filter the list of SOAP/XML transaction monitoring policies.
    + Create a new SOAP/XML transaction monitoring policy.
    + View a SOAP/XML transaction monitoring policy.
    + Update a SOAP/XML transaction monitoring policy.
    + Replace a SOAP/XML transaction monitoring policy.
    + Delete a SOAP/XML transaction monitoring policy.

  - Organizations

    + View/search/filter the list of organizations.
    + Create an organization.
    + View the properties of an organization.
    + Update the properties of an organization.
    + Replace an organization.
    + Delete an organization.
    + View/search/filter the list of logs associated with an organization.
    + View a log message associated with an organization.
    + View/search/filter the list of notes associated with an organization.
    + Add a note to an organization.
    + View a note associated with an organization.
    + Update a note associated with an organization.
    + Replace a note associated with an organization.
    + Delete a note associated with an organization.

  - Product SKUs

    + View/search/filter the list of Product SKUs.
    + Create a new Product SKU.
    + View a Product SKU.
    + Update a Product SKU.
    + Replace a Product SKU.
    + Delete a Product SKU.

  - Themes
    
    + View/search/filter the list of themes.
    + Create a new theme.
    + View a theme.
    + Update a theme.
    + Replace a theme.
    + Delete a theme.

  - Tickets

    + View/search/filter the list of tickets.
    + Create a new ticket.
    + View the properties of a ticket.
    + Replace a ticket.
    + Update a ticket.
    + View/search/filter the list of notes associated with a ticket.
    + Add a note to a ticket.
    + View a note associated with a ticket.
    + Update a note associated with a ticket.
    + Replace a note associated with a ticket.
    + Retrieve an attachment from a ticket note associated with a ticket.
    + Add an attachment to a ticket note associated with a ticket.
    + View/search/filter the list of external watchers associated with a ticket
    + Add an external watcher to a ticket.
    + View an external watcher associated with a ticket.
    + Update an external watcher associated with a ticket.
    + Replace an external watcher associated with a ticket.
    + Remove an external watcher from a ticket.
    + View/search/filter the list of organization watchers associated with a ticket
    + Add an organization watcher to a ticket.
    + View an organization watcher associated with a ticket.
    + Update an organization watcher associated with a ticket.
    + Replace an organization watcher associated with a ticket.
    + Remove an organization watcher from a ticket.
    + View/search/filter the list of ticket queue watchers associated with a ticket
    + Add a ticket queue watcher to a ticket.
    + View a ticket queue watcher associated with a ticket.
    + Update a ticket queue watcher associated with a ticket.
    + Replace a ticket queue watcher associated with a ticket.
    + Remove a ticket queue watcher from a ticket.

  - Ticket Categories
    
    + View/search/filter the list of ticket categories.
    + View the properties of a ticket category.

  - Ticket Chargeback
    
    + View/search/filter the list of ticket chargeback entries.
    + View the properties of a ticket chargeback entry.

  - Ticket Notes

    + View/search/filter the list of all ticket notes.
    + Create a new ticket note.
    + View the properties of a ticket note.
    + Update a ticket note.
    + Replace a ticket note.
    + Add an attachment to a ticket note.
    + Retrieve an attachment from a ticket note.
    + View/search/filter the list of all ticket notes.
    + Create a new ticket note.
    + View the properties of a ticket note.
    + Update a ticket note.
    + Replace a ticket note.
    + Add an attachment to a ticket note.
    + Retrieve an attachment from a ticket note.

  - Ticket Queues

    + View/search/filter the list of ticket queues.
    + Create a new ticket queue.
    + View the properties of a ticket queue.
    + Update a ticket queue.
    + Replace a ticket queue.
    + Delete a ticket queue.

  - Ticket States

    + View/search/filter the list of ticket states.
    + Create a new ticket state.
    + View the properties of a ticket state.
    + Update a ticket state.
    + Replace a ticket state.
    + Delete a ticket state.

  - User Policies

    + View/search/filter the list of user policies.
    + Create a new user policy.
    + View the properties of a user policy.
    + Update the properties of a user policy.
    + Replace a user policy.
    + Delete a user policy.

  - Vendors

    + View/search/filter the list of vendor records.
    + Create a new vendor record.
    + View a vendor record.
    + Update a vendor record.
    + Replace a vendor record.
    + Delete a vendor record.
