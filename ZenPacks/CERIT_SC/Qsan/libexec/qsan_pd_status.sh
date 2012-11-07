#!/bin/bash
SNMP_IP="$1"
SNMP_VER="$2"
SNMP_COMMUNITY="$3"
SNMP_TIMEOUT="$4"
SNMP_RETRIES="$5"
SNMP_INDEX="$6"

# get both data in single command
SNMP_DATA=$(snmpget -O qvU "-${SNMP_VER}" "-c${SNMP_COMMUNITY}" \
	"-t${SNMP_TIMEOUT}" "-r${SNMP_RETRIES}" \
	"${SNMP_IP}" \
	".1.3.6.1.4.1.22274.1.2.1.1.4.${SNMP_INDEX}" \
	".1.3.6.1.4.1.22274.1.2.1.1.5.${SNMP_INDEX}" 2>/dev/null | sed -e 's/"//g')

SNMP_DATA_COUNT=$(echo "$SNMP_DATA" | wc -l)

if [ "x${SNMP_DATA_COUNT}" = 'x2' ]; then
	STATE_TXT=$(echo "${SNMP_DATA}" | head -1)
	HEALTH_TXT=$(echo "${SNMP_DATA}" | tail -1)
else
	STATE_TXT=''
	HEALTH_TXT=''
fi

shopt -s nocasematch
case "${STATE_TXT}" in
	'')				STATE=0 ;;
	'Online')		STATE=1 ;;
	'Rebuiding')	STATE=2 ;;
	'Transition')	STATE=3 ;;
	'Scrubbing')	STATE=4 ;;
	*)				STATE=9 ;;
esac

case "${HEALTH_TXT}" in
	'')				HEALTH=0 ;;
	'Good')			HEALTH=1 ;;
	'Failed')		HEALTH=2 ;;
	'Error Alert')	HEALTH=3 ;;
	'Read Errors')	HEALTH=4 ;;
	*)				HEALTH=9 ;;
esac

echo "state:${STATE} health:${HEALTH}"
