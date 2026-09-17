# Security Policy

## Overview

OQubit is an open-source quantum computing and simulation library.

We take security issues seriously and encourage responsible disclosure of vulnerabilities that may affect OQubit users, installations, dependencies, or project infrastructure.

Please do not publicly disclose a suspected security vulnerability before it has been investigated and, where appropriate, a fix has been released.

## Supported Versions

Security fixes are generally applied to the latest maintained release and the active development branch.

| Version            | Supported    |
| ------------------ | ------------ |
| 0.1.0     | :white_check_mark: |

Because OQubit is under active development, the supported-version policy may change between releases.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub Issues, Discussions, or Pull Requests.**

### Preferred Method

Please report security vulnerabilities privately by email:

**[priyamghosh2009@outlook.com](mailto:priyamghosh2009@outlook.com)**

When reporting a vulnerability, please include `[SECURITY]` in the email subject.

### Example

```text
Subject: [SECURITY] Vulnerability in OQubit <component>
```

Please avoid publicly disclosing vulnerability details until the issue has been investigated and an appropriate fix or mitigation has been prepared.

## What to Include

Please provide as much relevant information as possible, including:

* A clear description of the vulnerability.
* The affected OQubit version, release, branch, or commit.
* The affected module, component, or file.
* Steps required to reproduce the issue.
* A minimal proof of concept, where appropriate.
* The expected and actual behavior.
* The potential security impact.
* Relevant Python, operating-system, or dependency versions.
* Any suggested mitigation or fix, if available.

Providing precise reproduction information helps the maintainer investigate and address reports efficiently.

## Responsible Disclosure

We ask security researchers to:

* Report vulnerabilities privately before public disclosure.
* Avoid accessing, modifying, or destroying data that does not belong to them.
* Avoid testing against systems or services without authorization.
* Avoid actions that could disrupt users or project infrastructure.
* Allow reasonable time for investigation and remediation.
* Avoid publicly sharing exploit details until coordinated disclosure is appropriate.

## Our Response

When a security report is received, the maintainer will make a reasonable effort to:

1. Acknowledge receipt of the report.
2. Review and reproduce the reported issue.
3. Determine affected versions and security impact.
4. Develop and test an appropriate fix where necessary.
5. Release a fix or mitigation when practical.
6. Credit the reporter when they request credit and disclosure permits it.
7. Coordinate public disclosure when appropriate.

Response and remediation times may vary depending on the complexity and severity of the issue.

## Security Advisories

When appropriate, confirmed vulnerabilities may be documented through GitHub Security Advisories.

Users should update to the recommended fixed version or apply the documented mitigation as soon as practical.

## Scope

This policy primarily covers:

* OQubit source code.
* Official OQubit Python packages and releases.
* OQubit build and distribution configuration.
* Security-relevant dependencies when their use creates an issue in OQubit.
* Official project infrastructure directly controlled by the OQubit project.

Issues unrelated to security should be reported through the project's normal issue tracker.

## No Bug Bounty

OQubit does **not currently operate a paid bug bounty program**.

Submitting a vulnerability report does not create an entitlement to monetary compensation.

## Recognition

We appreciate responsible security researchers and contributors who help improve OQubit.

With the reporter's permission, security contributors may be acknowledged in relevant release notes, security advisories, or project documentation.

## Contact

For security-related reports:

**[priyamghosh2009@outlook.com](mailto:priyamghosh2009@outlook.com)**

For general questions, feature requests, documentation issues, and non-security bugs, please use the appropriate public GitHub repository channels.

---

Thank you for helping keep OQubit and its users secure.