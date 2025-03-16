<!DOCTYPE html>
<html>
<head>
   <!-- <title>Test Case Development Table</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style> -->
</head>
<body>
    <h2>Test Case Development Table</h2>
    <table>
        <tr>
            <th>Test Case ID</th>
            <th>Requirement ID</th>
            <th>Description</th>
            <th>Steps ID</th>
            <th>Expected Result</th>
            <th>Actual Result</th>
            <th>Status (Pass/Fail)</th>
        </tr>
        <tr>
            <td>FR-001</td>
            <td>Login</td>
            <td>Login to the system with correct details.</td>
            <td>1. Enter username and password.<br>2. Click "Login".</td>
            <td>The system validates the login and allows user access.</td>
            <td>User is logged in successfully.</td>
            <td></td>
        </tr>
        <tr>
            <td>FR-001</td>
            <td>Login</td>
            <td>Login to the system with incorrect details.</td>
            <td>1. Enter incorrect username and password.<br>2. Click "Login".</td>
            <td>System issues error message "Incorrect username or password".</td>
            <td>System issues error message "Incorrect username or password".</td>
            <td></td>
        </tr>
        <tr>
            <td>FR-001</td>
            <td>Role-Based Access Control</td>
            <td>Admin tries to access patient medical records.</td>
            <td>1. Log in as admin.<br>2. Attempt to view patient medical records.</td>
            <td>System denies access and issues "User not authorized" message.</td>
            <td>System denied access correctly.</td>
            <td></td>
        </tr>
        <tr>
            <td>FR-002</td>
            <td>Patient Registration</td>
            <td>Register a new patient.</td>
            <td>1. Enter patient details.<br>2. Search for existing records.<br>3. Click "Register".</td>
            <td>New patient record is created and saved.</td>
            <td>Patient created successfully with unique ID.</td>
            <td></td>
        </tr>
        <tr>
            <td>FR-002</td>
            <td>Patient Registration</td>
            <td>Register an existing patient.</td>
            <td>1. Enter patient details.<br>2. Search for existing records.</td>
            <td>System displays message "Patient does exist with unique ID".</td>
            <td>System issued correct message.</td>
            <td></td>
        </tr>
        <tr>
            <td>FR-005</td>
            <td>Retrieve Patient History</td>
            <td>Doctor retrieves patient history.</td>
            <td>1. Search patient.<br>2. Click "View patient history".</td>
            <td>History is displayed within 20 seconds or message "No previous treatment or diagnosis found".</td>
            <td>Patient history displayed correctly.</td>
            <td></td>
        </tr>
        <tr>
            <td>NFR-001</td>
            <td>Performance Test</td>
            <td>Simulate 1,000 concurrent users searching.</td>
            <td>1. Simulate 1,000 users searching.<br>2. Measure response time.</td>
            <td>Response time should be ≤ 15 seconds.</td>
            <td>System responded within ≤ 15 seconds.</td>
            <td></td>
        </tr>
    </table>
</body>
</html>
