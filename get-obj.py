import oci

# Initialize the Object Storage client without any explicit configuration
object_storage_client = oci.object_storage.ObjectStorageClient({}, signer=oci.auth.signers.InstancePrincipalsSecurityTokenSigner())

# Specify the namespace, bucket name, and object name
namespace_name = "bmv5xptcmwel"
bucket_name = "bucket-20240416-1420"
object_name = "Abstract.txt"

try:
    # Retrieve the object
    get_object_response = object_storage_client.get_object(
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        object_name=object_name
    )

    # Read the object content as binary
    object_content = get_object_response.data.content

    # Print the binary content (this might display non-printable characters)
    print("Object content as binary:")
    print(object_content)

except Exception as e:
    print("error")










