using UnityEngine.Audio;
using System;
using UnityEngine;

public class AudioManager : MonoBehaviour
{
    /* --------------------------------------------------------------------------------------------
     * Usage:
     * In the place where you want to play the sound write
     * FindObjectOfType<AudioManager>().Play("name of sound file (without .ogg ending)")
     * 
     * What if you want the audio manager in multiple scenes?
     * Put the game object into the prefab folder and then drag it from there to the scenes you want
     * The if (instance...) handles the audio not cutting off when switching scenes
     * And the DontDestroy... makes sure there aren't multiple audio managers
     * ----------------------------------------------------------------------------------------------*/

    public Sound[] sounds;

    public static AudioManager instance;

    // Start is called before the first frame update
    void Awake()
    {
        if (instance == null)
        {
            instance = this;
        } else
        {
            Destroy(gameObject);
            return;
        }

        DontDestroyOnLoad(gameObject);

        foreach (Sound s in sounds)
        {
            s.source = gameObject.AddComponent<AudioSource>();
            s.source.clip = s.clip;
            s.source.volume = s.volume;
            s.source.pitch = s.pitch;
            s.source.loop = s.loop;
        }
    }

    void Start()
    {
        Play("9.ogg");
    }

    public void Play(string name)
    {
        Sound s = Array.Find(sounds, sound => sound.name == name);
        s.source.Play();
    }
}
