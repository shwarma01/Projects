using UnityEngine;

public class FollowPlayer : MonoBehaviour
{
    public Transform player;
    public Vector3 offset;

    // Update is called once per frame
    void Update()
    {
        // Non capital "t" means this object
        transform.position = player.position + offset;
    }
}
