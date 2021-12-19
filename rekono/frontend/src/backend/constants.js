const accessTokenKey = 'access-token'
const refreshTokenKey = 'refresh-token'

const stages = [
  { id: 1, value: 'OSINT' },
  { id: 2, value: 'Enumeration' },
  { id: 3, value: 'Vulnerabilities' },
  { id: 4, value: 'Services' },
  { id: 5, value: 'Exploitation' }
]

const findingTypes = ['OSINT', 'Host', 'Enumeration', 'Endpoint', 'Technology', 'Vulnerability', 'Exploit', 'Credential', 'Wordlist']

export {
  accessTokenKey,
  refreshTokenKey,
  stages,
  findingTypes
}
