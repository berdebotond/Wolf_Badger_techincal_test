# DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginGet**](DefaultApi.md#loginGet) | **GET** /login | Initiates the GitHub OAuth login process
[**loginGithubAuthorizedGet**](DefaultApi.md#loginGithubAuthorizedGet) | **GET** /login/github/authorized | Callback endpoint for GitHub OAuth authorization
[**logsErrorGet**](DefaultApi.md#logsErrorGet) | **GET** /logs/error | Retrieves error logs
[**profileGet**](DefaultApi.md#profileGet) | **GET** /profile | Retrieves the user profile information
[**userIdDelete**](DefaultApi.md#userIdDelete) | **DELETE** /user/{id} | Deletes a user by ID
[**userIdGet**](DefaultApi.md#userIdGet) | **GET** /user/{id} | Retrieves a user by ID
[**userIdPut**](DefaultApi.md#userIdPut) | **PUT** /user/{id} | Updates a user by ID
[**userPost**](DefaultApi.md#userPost) | **POST** /user | Creates a new user


<a name="loginGet"></a>
# **loginGet**
> loginGet()

Initiates the GitHub OAuth login process

Initiates the GitHub account login process using Flask Dance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.loginGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#loginGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirects the user to the GitHub login page. |  -  |

<a name="loginGithubAuthorizedGet"></a>
# **loginGithubAuthorizedGet**
> loginGithubAuthorizedGet()

Callback endpoint for GitHub OAuth authorization

Retrieves the access token after the user is redirected back from GitHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.loginGithubAuthorizedGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#loginGithubAuthorizedGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirects the user to the profile page. |  -  |

<a name="logsErrorGet"></a>
# **logsErrorGet**
> List&lt;ErrorLog&gt; logsErrorGet()

Retrieves error logs

Retrieves error logs from the application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<ErrorLog> result = apiInstance.logsErrorGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logsErrorGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ErrorLog&gt;**](ErrorLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON array containing error log entries. |  -  |

<a name="profileGet"></a>
# **profileGet**
> profileGet()

Retrieves the user profile information

Fetches the user&#39;s profile information from GitHub.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.profileGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#profileGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON object containing the user&#39;s profile information. |  -  |
**401** | Unauthorized - User not authenticated. |  -  |

<a name="userIdDelete"></a>
# **userIdDelete**
> userIdDelete(id)

Deletes a user by ID

Deletes a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | ID of the user to delete.
    try {
      apiInstance.userIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Long**| ID of the user to delete. |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty response with a success status. |  -  |
**401** | Unauthorized - User not authenticated. |  -  |
**404** | Not Found - User with the given ID not found. |  -  |

<a name="userIdGet"></a>
# **userIdGet**
> userIdGet(id)

Retrieves a user by ID

Retrieves a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | ID of the user to retrieve.
    try {
      apiInstance.userIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Long**| ID of the user to retrieve. |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON object containing the user details. |  -  |
**401** | Unauthorized - User not authenticated. |  -  |
**404** | Not Found - User with the given ID not found. |  -  |

<a name="userIdPut"></a>
# **userIdPut**
> userIdPut(id, user)

Updates a user by ID

Updates a user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | ID of the user to update.
    UserInput user = new UserInput(); // UserInput | JSON object representing the user details to be updated.
    try {
      apiInstance.userIdPut(id, user);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Long**| ID of the user to update. |
 **user** | [**UserInput**](UserInput.md)| JSON object representing the user details to be updated. |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON object containing the updated user details. |  -  |
**400** | Bad Request - Invalid input data or missing required fields. |  -  |
**401** | Unauthorized - User not authenticated. |  -  |
**404** | Not Found - User with the given ID not found. |  -  |

<a name="userPost"></a>
# **userPost**
> userPost(user)

Creates a new user

Creates a new user if the user is authenticated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UserInput user = new UserInput(); // UserInput | JSON object representing the user details.
    try {
      apiInstance.userPost(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UserInput**](UserInput.md)| JSON object representing the user details. |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The ID of the created user. |  -  |
**400** | Bad Request - Invalid input data or missing required fields. |  -  |
**401** | Unauthorized - User not authenticated. |  -  |

