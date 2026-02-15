---
title: Authentication | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/authentication
source: sitemap
fetched_at: 2026-02-15T09:03:38.761664-03:00
rendered_js: false
word_count: 998
summary: This document provides instructions for authenticating with the AB Connect API using HMAC SHA-256 signatures and outlines security best practices for managing credentials.
tags:
    - api-authentication
    - hmac-sha256
    - ab-connect
    - signature-generation
    - api-security
    - rest-api
category: guide
---

In order to use the interactive [Reference section](https://developerdocs.instructure.com/services/ab-connect/reference/standards), you will need to properly authenticate. If you do not have credentials, you can [request a sandbox accountarrow-up-right](https://community.canvaslms.com/plugins/custom/instructure/instructure/custom.ab-form). Alternatively, you can inquire about purchasing a license, or request access for your company's account, via [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Question%20or%20Comment%20%28v4.1%20API%29).

Once you have your partner ID and key, you can create signatures and start to make calls to the production version of AB Connect. From a high level, the signature is an HMAC SHA-256 hash of a message constructed in a specific format. Use the partner key that is given to you by AB Support for the hash key. The message has one required field (expires - expressed in seconds since epoch) and three optional values: user, method and resource. The delimiter between the fields is a bare newline character (no carriage return) typically denoted as "\\n". The generalized form of the message is:

`<expires>[\nuser][\nmethod][\nresource]`

Here are some example messages and their interpretation:

- `1508419888` - Access expires on October 19th 2017 at 1:31:28 PM ET. Note that expirations are expressed in Eastern time in the US.
- `1508419888\nbmarley` - Same expiration time but the signature is only valid for Bob Marley's account. Note that if you supply a user, the user.id field must include the same value in the URL parameters.
- `1508419888\n\nGET` - This signature can only be used for GET HTTP requests. Notice that the method is uppercase. This is a good approach when using AB Connect from public (or customer) facing web clients. It ensures that a hacker can't manipulate your Assets.
- `1508419888\n\nGET\nstandards` - This signature can only be used for GET requests to standards. Notice that the resource is lowercase. If you have a web client that allows users to browse standards but you want to keep your Asset metadata profiles private, this will limit the scope accordingly.

NOTES:

- Each field can have only one value, so you can't mix methods or support multiple endpoints. E.g. if you want to allow read access to both Standards and Topics, you'll need to create two signatures and use the appropriate signature for each call.
- While the expires (`auth.expires`), signature (`auth.signature`) and optionally the user (`user.id`) are included in the URL parameters, the method and resource values are inferred from the actual call being made so there is no need to pass those as URL parameters.
- If you specify a resource, you must specify a method. Allowing "all methods" on one endpoint is not currently supported. So, for example, your message can not look like `1508419888\n\n\nassets`.

Once you have calculated the signature, include the authentication parameters in the URL of your call to AB Connect. The general form of the parameters is:

`&partner.id=<ID>&auth.signature=<signature generated above>&auth.expires=<signature expiry in seconds since epoch>`

or if you are including a user ID:

`&partner.id=<ID>&auth.signature=<signature generated above>&auth.expires=<signature expiry in seconds since epoch>&user.id=<user>`

So if your partner ID is `test_account` and your key is `ajk84Hjk93h59skaAJ8732` and you want to generate a read-only signature that expires on Wed Dec 06 2017 09:20:29 GMT-0500 (Eastern Standard Time)...

- Your message would be: `1512570029\n\nGET`
- Your signature would be a base64 encoding of the HMAC SHA-256 hash of the message: `Sdcfa9xgRAUzQnlLik5nKj1ntqdB85jFYyFCkNxwD/M=`
- URL encoding each parameter value and assembling the parameters together, the authentication portion of the URL would be: `&partner.id=test_account&auth.signature=Sdcfa9xgRAUzQnlLik5nKj1ntqdB85jFYyFCkNxwD%2FM%3D&auth.expires=1512570029`

You can use the following code examples as a starting point for constructing an authentication signature for use when calling AB Connect. Note that these examples do not necessarily follow coding best-practices - e.g. they do not have proper error handling in place. They are intended to be simple examples to show the concepts necessary to perform API authentication. Also note that these examples don't include any method or resource limiters in the signature.

## Best Practices for Web Clients

Due to the nature of web clients, anything available to the client application can be accessed by the user. The user can view the source and use Inspect/Developer mode to access variable values, etc. For this reason, you need to be particularly careful with security measures. If you are accessing AB Connect directly from a web client, consider the following when creating your signatures:

- Keep your partner key secret. Don't send it to the web client for any reason. If someone malicious gets a hold of your partner key, they can create any signature they want at any time they want and do damage to your Asset profiles. If you suspect your partner key has been compromised, contact AB Support and ask to have a new partner key issued.
- Keeping your partner key secure means you need to generate the signature on the server side and embed the signature in the page as it is served to the client. Alternatively, you can create a service that generates signatures on request for your web clients. However, if you do that, you'll need to layer your own security model on top of that to ensure the web client making the request has permissions to access the AB Connect signature.
- Make the life of the signature reasonably short. What is reasonable for your situation is up to you. Perhaps limit read capabilities to an hour and update (POST, PATCH, DELETE) to a few minutes. One thing to consider what is the user experience with the signature expires. Does the page force a re-load to gain a new token? Does it make an authenticated call to your server via AJAX to renew the signature? Does the user need to re-authenticate or do you trust a session cookie?
- Limit the method to the minimum required capabilities. Most web clients will only need read access (e.g. if you are offering the user a Standards or Asset browser). If you need to change permissions, consider creating a separate, short-lived signature for those situations.

See also the C# example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    using System;
    using System.IO;
    using System.Net;
    using System.Security.Cryptography;
    using System.Text;
    class Program
      {
      static void Main(string[] args)
      {
        var partnerID = "public";                   // ID provided by AB.
        var partnerKey = "2jfaWErgt2+o48gsk302kd";  // Key provided by AB.
        var userID = "Bob";                         // Optional. Partner defined string. Provides access only for queries with this `user.id`.
        // Seconds since epoch. Example is 24 hours.
        var expires = (long)Math.Floor(
          (DateTime.UtcNow.AddHours(24) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds
        );
        var message = string.Format("{0}\n{1}", expires, userID);
        var keyBytes = Encoding.UTF8.GetBytes(partnerKey);
        var messageBytes = Encoding.UTF8.GetBytes(message);
        string signature;
        using (var hmac = new HMACSHA256(keyBytes))
        {
          signature = Convert.ToBase64String(hmac.ComputeHash(messageBytes));
        }
        var requestBuilder = new UriBuilder("https://api.abconnect.instructure.com/rest/v4.1/standards");
        // user.id is optional
        requestBuilder.Query = string.Format(
          "partner.id={0}&auth.signature={1}&auth.expires={2}&user.id={3}",
          WebUtility.UrlEncode(partnerID),
          WebUtility.UrlEncode(signature),
          expires,
          WebUtility.UrlEncode(userID)
        );
        var request = WebRequest.Create(requestBuilder.Uri);
        Console.WriteLine(new StreamReader(request.GetResponse().GetResponseStream()).ReadToEnd());
      }
    }
```

See also the Perl example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    #!/usr/bin/perl
    use strict;
    use Digest::SHA qw(hmac_sha256_base64);
    use LWP::UserAgent;
    my $partner_id = 'public';                  # ID provided by AB.
    my $partner_key = '2jfaWErgt2+o48gsk302kd'; # Key provided by AB.
    my $expires = time() + 86400;               # Seconds since epoch. Example is 24 hours.
    my $user_id = 'Bob';                        # Optional. Partner defined string. Provides access only for queries with this `user.id`.
    my $message = "$expires\n$user_id";
    my $signature = hmac_sha256_base64($message, $partner_key);
    my $uri = URI->new();
    $uri->scheme('https');
    $uri->host('api.abconnect.instructure.com');
    $uri->port(443);
    $uri->path('rest/v4.1/standards');
    # user.id is optional
    $uri->query_form(
      'partner.id'     => $partner_id,
      'auth.signature' => $signature,
      'auth.expires'   => $expires,
      'user.id'        => $user_id
    );
    my $req = HTTP::Request->new(GET => $uri);
    my $ua = LWP::UserAgent->new();
    my $response = $ua->request($req);
    print 'response code = '.$response->{_rc}."\n";
    if ($response->{_rc} && ($response->{_rc} == 200)) {
      if ($response->{_content}) {
        print $response->{_content};
      }
    }
```

See also the PHP example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    <!DOCTYPE html>
    <HTML>
    <HEAD>
    </HEAD>
    <BODY>
      <?php
        $partnerID   = 'public';                  // ID provided by AB.
        $partnerKey  = '2jfaWErgt2+o48gsk302kd';  // Key provided by AB.
        $authExpires = time() + 3600;             // Seconds since epoch. Example is 1 hour.  Keep this shorter due to web exposure.
        $userID      = 'Bob';                     // Optional. Partner defined string. Provides access only for queries with this `user.id`.
        $url = 'https://api.abconnect.instructure.com/rest/v4.1/standards?';
        $url .= 'partner.id=' . $partnerID;
        // "GET" results read only signature to minimize security risks with web client exposure.
        $message = $authExpires . "\n" . $userID . "\n" . "GET";
        $sig = urlencode(base64_encode(hash_hmac('sha256', $message, $partnerKey, true))); // build the signature with the key
        $url .= '&auth.signature=' . $sig;
        $url .= '&auth.expires=' . $authExpires;
        if ($url) {
          $url .= '&user.id=' . $userID;
        }
        print '<H3>Generated Request URL</H3>';
        print '<P>' . $url . '</P><BR />';
        $response = file_get_contents($url);
        print '<H3>JSON Response</H3>';
        print '<P>' . $response . '</P>';
      ?>
    </BODY>
    </HTML>
```

See also the Python2 example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    import time
    import hashlib
    import hmac
    import base64
    import urllib
    partner_id = 'public'                    # ID provided by AB.
    partner_key = '2jfaWErgt2+o48gsk302kd'   # Key provided by AB.
    expires = str(int(time.time() + 86400))  # Seconds since epoch. Example expires in 24 hours.
    user_id = 'Bob'                          # Optional. Partner defined string. Provides access only for queries with this `user.id`.
    message = expires + "\n" + user_id
    digest = hmac.new(partner_key.encode(), message.encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    encoded_sig = urllib.quote_plus(signature)
    # user.id is optional
    parms = 'partner.id=' + partner_id + \
            '&auth.signature=' + encoded_sig + \
            '&auth.expires=' + expires + \
            '&user.id=' + user_id
    result = urllib.urlopen('https://api.abconnect.instructure.com/rest/v4.1/standards?' + parms).read()
    print result
```

See also the Python3 example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    import time
    import hashlib
    import hmac
    import base64
    import urllib.request
    partner_id = 'public'                    # ID provided by AB.
    partner_key = '2jfaWErgt2+o48gsk302kd'   # Key provided by AB.
    expires = str(int(time.time() + 86400))  # Seconds since epoch. Example expires in 24 hours.
    user_id = 'Bob'                          # Optional. Partner defined string. Provides access only for queries with this `user.id`.
    message = expires + "\n" + user_id
    digest = hmac.new(partner_key.encode(), message.encode(), digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()
    encoded_sig = urllib.parse.quote_plus(signature)
    # user.id is optional
    parms = 'partner.id=' + partner_id + \
            '&auth.signature=' + encoded_sig + \
            '&auth.expires=' + expires + \
            '&user.id=' + user_id
    result = urllib.request.urlopen('https://api.abconnect.instructure.com/rest/v4.1/standards?' + parms).read()
    print (result)
```

See also the VB example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    Imports System.Security.Cryptography
    Imports System.Text
    Imports System.Net
    Imports System.IO
    Module AuthModule
        Sub Main()
            Dim PartnerId As String = "public"                  ' ID provided by AB.
            Dim PartnerKey As String = "2jfaWErgt2+o48gsk302kd" ' Key provided by AB.
            Dim UserId As String = "Bob"                        ' Optional. Partner defined string. Provides access only for queries with this `user.id`.
            ' Seconds since epoch. Example is 24 hours.
            Dim Expires = Math.Floor(
              (DateTime.UtcNow.AddHours(24) - New DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds
            )
            Dim Message = Expires & vbLf & UserId
            Dim KeyBytes() As Byte = Encoding.UTF8.GetBytes(PartnerKey)
            Dim MessageBytes() As Byte = Encoding.UTF8.GetBytes(Message)
            Dim Signature As String
            Using myHMACSHA256 As New HMACSHA256(KeyBytes)
                Signature = Convert.ToBase64String(myHMACSHA256.ComputeHash(MessageBytes))
            End Using
            Dim RequestBuilder As New UriBuilder("https://api.abconnect.instructure.com/rest/v4.1/standards")
            ' user.id is optional
            RequestBuilder.Query = String.Format(
              "partner.id={0}&auth.signature={1}&auth.expires={2}&user.id={3}",
              WebUtility.UrlEncode(PartnerId),
              WebUtility.UrlEncode(Signature),
              Expires,
              WebUtility.UrlEncode(UserId)
            )
            Dim Request = WebRequest.Create(RequestBuilder.Uri)
            Dim Response As WebResponse = Request.GetResponse()
            Dim ReceiveStream As Stream = Response.GetResponseStream()
            Dim Encode As Encoding = Encoding.GetEncoding("utf-8")
            Dim ReadStream As New StreamReader(ReceiveStream, Encode)
            Dim ReadBuffer(256) As [Char]
            Dim Count As Integer = ReadStream.Read(ReadBuffer, 0, 256)
            While Count > 0
                Dim StringData As New [String](ReadBuffer, 0, Count)
                Console.Write(StringData)
                Count = ReadStream.Read(ReadBuffer, 0, 256)
            End While
            Console.WriteLine("")
        End Sub
    End Module
```

See also the Java example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    package AuthExample;
    import java.io.BufferedReader;
    import java.io.InputStream;
    import java.io.InputStreamReader;
    import java.net.URL;
    import java.net.URLEncoder;
    import java.util.Base64;
    import java.util.Calendar;
    import java.util.TimeZone;
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    import javax.net.ssl.HttpsURLConnection;
    public class program {
      public static void main(String[] args) {
        String partnerID = "public";                   // ID provided by AB.
        String partnerKey = "2jfaWErgt2+o48gsk302kd";  // Key provided by AB.
        String userID = "Bob";                         // Optional. Partner defined string. Provides access only for queries with this `user.id`.
        // Seconds since epoch. Example is 24 hours.
        Calendar cal = Calendar.getInstance(TimeZone.getTimeZone("GMT"));
        long expires = (long)Math.floor(cal.getTimeInMillis() / 1000) + 60*60*24;
        String message = String.format("%d\n%s", expires, userID); // format message for signature
        HttpsURLConnection connection = null;
        try {
          //
          // generate signature and base64 encode it
          //
          Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
          SecretKeySpec secret_key = new SecretKeySpec(partnerKey.getBytes("UTF-8"), "HmacSHA256");
          sha256_HMAC.init(secret_key);
          byte[] hmacBytes = sha256_HMAC.doFinal(message.getBytes("UTF8"));
          String signature = Base64.getEncoder().encodeToString(hmacBytes);
          //
          // pack the signature and other auth parameters in URL
          //
          String targetURL = String.format(
            "https://api.abconnect.instructure.com/rest/v4.1/standards?partner.id=%s&auth.signature=%s&auth.expires=%d&user.id=%s",
            URLEncoder.encode(partnerID, "UTF-8"),
            URLEncoder.encode(signature, "UTF-8"),
            expires,
            URLEncoder.encode(userID, "UTF-8")
            );
          //
          //Create connection
          //
          URL url = new URL(targetURL);
          connection = (HttpsURLConnection) url.openConnection();
          //
          // Get Response
          //
          InputStream is = connection.getInputStream();
          BufferedReader rd = new BufferedReader(new InputStreamReader(is));
          String line;
          while ((line = rd.readLine()) != null) {
            System.out.println(line);
          }
          rd.close();
        } catch (Exception e) {
          e.printStackTrace();
          System.exit(-1);
        } finally {
          if (connection != null) {
            connection.disconnect();
          }
        }
      }
    }
```

See also the NodeJS example project in the authentication folder of our [github repositoryarrow-up-right](https://github.com/instructure/abconnect-samples).

```
    #!/usr/bin/env node
    var partner_id = 'public'                             // ID provided by AB.
    var partner_key = '2jfaWErgt2+o48gsk302kd'            // Key provided by AB.
    var expires = Math.floor(Date.now() / 1000) + 86400;  // Seconds since epoch. Example expires in 24 hours.
    var user_id = 'Bob'                                   // Optional. Partner defined string. Provides access only for queries with this `user.id`.
    //
    // Build the signature
    //
    var message = '' + expires;
    if (user_id) {
        message +=  "\n" + user_id;
    }
    var crypto = require('crypto');
    var signature = crypto.createHmac('SHA256', partner_key).update(message).digest('base64')
    //
    // package the signature, expiration, etc. into a URL encoded query string fragment
    //
    var queryString = '&partner.id=' + encodeURIComponent(partner_id) + '&auth.signature=' + encodeURIComponent(signature) + '&auth.expires=' + encodeURIComponent(expires);
    if (user_id) {
        queryString += '&user.id=' + encodeURIComponent(user_id);
    }
    console.log("Authentication parameters: " + queryString);
    var requester = require('sync-request');
    var response;
    var body;
    try {
      response = requester('GET', 'https://api.abconnect.instructure.com/rest/v4.1/standards?' + queryString);
      body = response.getBody('utf-8');
    } catch (e) {
      console.log('' + e);
    }
    if (response) console.log("Response code: " + response.statusCode);
    if (body) console.log("Response body:\n" + body);
```

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).