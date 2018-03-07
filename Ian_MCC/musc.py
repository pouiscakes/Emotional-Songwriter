#!/usr/bin/env python

from midiutil.MidiFile import *
from midi2audio import FluidSynth


tonic = 62
degreesMajor  = [tonic, tonic+2, tonic+4, tonic+5, tonic+7, tonic+9, tonic+11, tonic+12] # MIDI note number
degreesMinor  = [tonic, tonic+2, tonic+3, tonic+5, tonic+7, tonic+8, tonic+11, tonic+12]
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 80   # In BPM
volume   = 100 # 0-127, as per the MIDI standard

joy = MIDIFile(1)
pop = MIDIFile(1)
sad = MIDIFile(1)


joy.addTempo(track, time, tempo)
pop.addTempo(track, time, tempo)
sad.addTempo(track, time, tempo)

def chordify(midifile, track, channel, rootnote, time, duration, volume, degrees):
	if rootnote == degrees[0]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[2], time, duration, volume)
		midifile.addNote(track, channel, degrees[4], time, duration, volume)
	if rootnote == degrees[1]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[3], time, duration, volume)
		midifile.addNote(track, channel, degrees[5], time, duration, volume)
	if rootnote == degrees[2]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[4], time, duration, volume)
		midifile.addNote(track, channel, degrees[6]-12, time, duration, volume)
	if rootnote == degrees[3]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[5]-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[0], time, duration, volume)
	if rootnote == degrees[4]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[1], time, duration, volume)
		midifile.addNote(track, channel, degrees[6]-12, time, duration, volume)
	if rootnote == degrees[5]:
		midifile.addNote(track, channel, rootnote, time, duration, volume)
		midifile.addNote(track, channel, rootnote-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[0], time, duration, volume)
		midifile.addNote(track, channel, degrees[2], time, duration, volume)
	if rootnote == degrees[6]:
		midifile.addNote(track, channel, degrees[6]-12-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[6]-12, time, duration, volume)
		midifile.addNote(track, channel, degrees[1], time, duration, volume) 
		midifile.addNote(track, channel, degrees[3], time, duration, volume) 

def joyProgression(midifile, track, channel, time, volume, degrees):
	for i in range(3):
		chordify(midifile, track, channel, degreesMajor[0], time, 0.5, volume, degreesMajor)
		time = time + 1
		chordify(midifile, track, channel, degreesMajor[0], time, 0.5, volume, degreesMajor)
		time = time + 1
		chordify(midifile, track, channel, degreesMajor[4], time, 0.5, volume, degreesMajor)
		time = time + 1
		chordify(midifile, track, channel, degreesMajor[4], time, 0.5, volume, degreesMajor)
		time = time + 1
	chordify(midifile, track, channel, degreesMajor[0], time, 2, volume, degreesMajor)
	time = time + 2
	midifile.addNote(track, channel, 128, time, 2, volume) # just so there is a rest at the end

def popProgression(midifile, track, channel, time, volume, degrees):
	chordify(midifile, track, channel, degreesMajor[0], time, 2, volume, degreesMajor)
	time = time + 2
	chordify(midifile, track, channel, degreesMajor[4], time, 2, volume, degreesMajor)
	time = time + 2
	chordify(midifile, track, channel, degreesMajor[5], time, 2, volume, degreesMajor)
	time = time + 2
	chordify(midifile, track, channel, degreesMajor[3], time, 2, volume, degreesMajor)
	time = time + 2
	chordify(midifile, track, channel, degreesMajor[0], time, 2, volume, degreesMajor)
	time = time + 2
	midifile.addNote(track, channel, 128, time, 2, volume) # just so there is a rest at the end

def sadProgression(midifile, track, channel, time, volume, degrees):
	chordify(midifile, track, channel, degreesMinor[0], time, 4, volume, degreesMinor)
	time = time + 4
	chordify(midifile, track, channel, degreesMinor[5], time, 4, volume, degreesMinor)
	time = time + 4
	chordify(midifile, track, channel, degreesMinor[0], time, 4, volume, degreesMinor)
	time = time + 4
	chordify(midifile, track, channel, degreesMinor[6], time, 4, volume, degreesMinor)
	time = time + 4
	chordify(midifile, track, channel, degreesMinor[0], time, 4, volume, degreesMinor)
	time = time + 4
	midifile.addNote(track, channel, 128, time, 2, volume) # just so there is a rest at the end



joyProgression(joy, track, channel, time, volume, degreesMajor)
with open("progressions/joyProgression.mid", "wb") as output_file:
    joy.writeFile(output_file)

popProgression(pop, track, channel, time, volume, degreesMajor)
with open("progressions/popProgression.mid", "wb") as output_file:
    pop.writeFile(output_file)

sadProgression(sad, track, channel, time, volume, degreesMinor)
with open("progressions/sadProgression.mid", "wb") as output_file:
    sad.writeFile(output_file)

fs = FluidSynth('soundfonts/S/JR_elepiano.sf2')
#fs.play_midi("progressions/joyProgression.mid")
fs.midi_to_audio('progressions/joyProgression.mid', 'bounces/joyProgression.wav')
fs = FluidSynth('soundfonts/S/JR_elepiano.sf2')
#fs.play_midi("progressions/joyProgression.mid")
fs.midi_to_audio('progressions/popProgression.mid', 'bounces/popProgression.wav')
fs = FluidSynth('soundfonts/S/JR_String2.sf2')
#fs.play_midi("progressions/joyProgression.mid")
fs.midi_to_audio('progressions/sadProgression.mid', 'bounces/sadProgression.wav')
