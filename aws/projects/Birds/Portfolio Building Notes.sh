Portfolio Building Session
Project-006 : Birds Carousel Static Website deploy on AWS Cloudfront, S3 and Route 53 using Cloudformation

Parameters

 - Domain Name ex. clarusway.us
 - Website Domain Name ex. birds.techtoyousoon.com

- S3
 - Bucket
 - Bucket Policy

- Cloudfront
 - Cloudfront Distribution

- Route 53
 - RecordSet for Website

- Certificate Manager
 - Certificate


Certificate Transparency is an open framework for monitoring and auditing certificates issued by Certificate Authorities in near real time. By requiring a CA to log all certificates they issue, site owners can quickly identify erroneously issued certificates, making detecting a rogue CA much easier.

If you do not use a protocol such as TLS/SSL, where the sent packet is encrypted from end to end, your website accesses can be read and changed in all the paths that this request packet takes until it reaches the destination. The first purpose of the TLS/SSL protocol is to prevent this. Of course, it doesn't just do that. It is also used for authentication and authorization.

In a web traffic without SSL/TLS, since the packet that comes out of your browser for website navigation and the response to this packet can be seen/changed at all transfer points, those who have both the authority and the technical means to keep these points will choose which websites and which websites on these websites. can easily see that you have requested access to its resources; If the legal authority has a decision to access these resources, they can easily implement it. That is, on an X site, you are allowed to see Y news; You may be blocked from seeing the Z news; You can see a note on the judicial decision at the page access.

However, if SSL/TLS is used and implemented correctly, since the content of your package cannot be seen at these transfer points; For example, the authorities will have to block access to these sites as a whole, since they know that you have accessed the Wikipedia site and cannot predict which articles you want to access on this site.

-----------

SSL/TLS offers end-to-end encryption, providing a convenient way for integrity, confidentiality, and authorization. In an ideal SSL implementation, we can be sure that the data transferred throughout the traffic does not change during the transfer, cannot be viewed by a third party, and that the person we are communicating with is indeed the person we desire.

In summary, in an ideal TLS/SSL implementation, your web traffic cannot be read or changed by any intervening third person/institution.