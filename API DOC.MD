## Authentication

### Refresh Token

- **Endpoint:** `/auth/token/refresh/`
- **Description:** Refresh an existing access token.
- **HTTP Method:** POST

### Verify Token

- **Endpoint:** `/auth/token/verify/`
- **Description:** Verify the validity of an access token.
- **HTTP Method:** POST

### User Registration

- **Endpoint:** `/auth/register/`
- **Description:** Register a new user.
- **HTTP Method:** POST

### Login

- **Endpoint:** `/auth/login/`
- **Description:** Obtain an access token by providing valid credentials.
- **HTTP Method:** POST

### Get All Users

- **Endpoint:** `/auth/users/`
- **Description:** Get a list of all users.
- **HTTP Method:** GET

### Assign Admin Privilege

- **Endpoint:** `/auth/assign-admin/`
- **Description:** Assign admin privileges to a user.
- **HTTP Method:** POST

## Cloud Services

### Cloud Services API Endpoints

All Cloud Services API endpoints are accessible under `/services`.

- **Cloud Service:** `/services/cloud-services/`

  - Description: Endpoint for CRUD operations on Cloud Services.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Storage:** `/services/cloud-storage/`

  - Description: Endpoint for CRUD operations on Cloud Storage.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Compute:** `/services/cloud-compute/`

  - Description: Endpoint for CRUD operations on Cloud Compute.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Database:** `/services/cloud-database/`

  - Description: Endpoint for CRUD operations on Cloud Database.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Analytics:** `/services/cloud-analytics/`

  - Description: Endpoint for CRUD operations on Cloud Analytics.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Networking:** `/services/cloud-networking/`

  - Description: Endpoint for CRUD operations on Cloud Networking.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

- **Cloud Security:** `/services/cloud-security/`
  - Description: Endpoint for CRUD operations on Cloud Security.
  - HTTP Methods: GET, POST, PUT, PATCH, DELETE

## Subscription Plans and Permissions

### Subscription Plans API Endpoints

- **Get All Plans and Create a New Plan:**

  - Endpoint: `/subscriptions/plans/`
  - Description: Endpoint for listing all subscription plans and creating a new plan.
  - HTTP Methods: GET, POST

- **Get a Particular Plan Details, Update a Plan, and Delete a Plan:**
  - Endpoint: `/subscriptions/plans/<int:pk>/`
  - Description: Endpoint for retrieving, updating, and deleting a specific subscription plan.
  - HTTP Methods: GET, PUT, PATCH, DELETE

### User Subscriptions API Endpoints

- **Get All Subscriptions and Create a New Subscription:**

  - Endpoint: `/subscriptions/`
  - Description: Endpoint for listing all user subscriptions and creating a new subscription.
  - HTTP Methods: GET, POST

- **Get a Particular Subscription Details, Update a Subscription, and Delete a Subscription:**
  - Endpoint: `/subscriptions/<int:pk>/`
  - Description: Endpoint for retrieving, updating, and deleting a specific user subscription.
  - HTTP Methods: GET, PUT, PATCH, DELETE

### Permissions API Endpoints

- **Get All Permissions and Create a New Permission:**

  - Endpoint: `/permissions/`
  - Description: Endpoint for listing all permissions and creating a new permission.
  - HTTP Methods: GET, POST

- **Get a Particular Permission Details, Update a Permission, and Delete a Permission:**
  - Endpoint: `/permissions/<int:pk>/`
  - Description: Endpoint for retrieving, updating, and deleting a specific permission.
  - HTTP Methods: GET, PUT, PATCH, DELETE

### Check User Permissions

- **Check Access Permissions of a User:**
  - Endpoint: `/access/<int:userId>/<int:pid>`
  - Description: Endpoint for checking access permissions of a user for a specific permission.
  - HTTP Method: GET
