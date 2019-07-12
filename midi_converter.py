import pretty_midi
import os

#inputフォルダから読み込む
inpath = 'input/'
#outputフォルダから読み込む
outpath = 'output'
flist = os.listdir(inpath)
for title in flist:
	print(title)
	# MIDIファイルのロード
	midi_data = pretty_midi.PrettyMIDI(inpath + title)
	# 新しいMIDIファイルの構築
	newmidi = pretty_midi.PrettyMIDI()
	piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
	piano = pretty_midi.Instrument(program=piano_program)

	for instrument in midi_data.instruments:
	    # ドラムでないトラックの音をpianoに入れる（ノートを入れる）
	    if not instrument.is_drum:
	        for note in instrument.notes:
	            piano.notes.append(note)

	#ノートを新しく生成したMIDIオブジェクトに入れる
	newmidi.instruments.append(piano)
	# outputディレクトリがなければ作成
	if not os.path.isdir(outpath):
	    os.mkdir(outpath)
	# 該当曲のディレクトリを作成
	newmidi.write(outpath + '/' + str(title))
