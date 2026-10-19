from pathlib import Path

p = Path("app/src/main/assets/index.html")
s = p.read_text()

if 'id="manualEditor"' in s:
    print("Panel Edit Manual sudah terpasang.")
    raise SystemExit

anchor = '<div class="group"><h3>3. Estimasi Biaya Proyek</h3>'

panel = """
<div class="group" id="manualEditor">
<h3>3. Edit Manual 3D</h3>
<label>Pilih elemen</label>
<select id="editTarget"></select>
<div class="row">
<div><label>Posisi X (m)</label><input id="editX" type="number" step="0.1"></div>
<div><label>Posisi Y (m)</label><input id="editY" type="number" step="0.1"></div>
</div>
<div class="row">
<div><label>Posisi Z (m)</label><input id="editZ" type="number" step="0.1"></div>
<div><label>Rotasi Y (derajat)</label><input id="editRotY" type="number" step="5"></div>
</div>
<div class="row">
<div><label>Skala X</label><input id="editScaleX" type="number" min="0.1" step="0.1"></div>
<div><label>Skala Y</label><input id="editScaleY" type="number" min="0.1" step="0.1"></div>
</div>
<label>Skala Z</label><input id="editScaleZ" type="number" min="0.1" step="0.1">
<button class="primary" id="editApply" type="button">Terapkan Perubahan</button>
<button class="secondary" id="editRefresh" type="button">Muat Posisi</button>
<p class="note">X = kiri/kanan, Y = atas/bawah, Z = depan/belakang.</p>
</div>
"""

if anchor not in s:
    raise SystemExit("Bagian RAB tidak ditemukan. File tidak diubah.")

s = s.replace(anchor, panel + anchor, 1)

js = r"""
function refreshEditTargets(){
 const sel=$('editTarget'),old=sel.value;
 sel.innerHTML='';
 extras.forEach((g,i)=>{
   const op=document.createElement('option');
   op.value=String(i);
   op.textContent=(i+1)+'. '+(g.userData.type||'elemen')+' - '+(g.userData.side||'');
   sel.appendChild(op);
 });
 if(!extras.length){
   sel.add(new Option('Belum ada elemen',''));
 }
 sel.value=[...sel.options].some(o=>o.value===old)?old:(extras.length?String(extras.length-1):'');
 syncEditFields();
}
function syncEditFields(){
 const g=extras[Number($('editTarget').value)];
 const ids=['editX','editY','editZ','editRotY','editScaleX','editScaleY','editScaleZ'];
 $('editApply').disabled=!g;
 ids.forEach(id=>$(id).disabled=!g);
 if(!g)return;
 $('editX').value=g.position.x.toFixed(2);
 $('editY').value=g.position.y.toFixed(2);
 $('editZ').value=g.position.z.toFixed(2);
 $('editRotY').value=(g.rotation.y*180/Math.PI).toFixed(1);
 $('editScaleX').value=g.scale.x.toFixed(2);
 $('editScaleY').value=g.scale.y.toFixed(2);
 $('editScaleZ').value=g.scale.z.toFixed(2);
}
$('editTarget').addEventListener('change',syncEditFields);
$('editRefresh').addEventListener('click',syncEditFields);
$('editApply').addEventListener('click',()=>{
 const g=extras[Number($('editTarget').value)];
 if(!g)return;
 const n=id=>Number($(id).value);
 const ids=['editX','editY','editZ','editRotY','editScaleX','editScaleY','editScaleZ'];
 if(ids.some(id=>!Number.isFinite(n(id)))||
    ['editScaleX','editScaleY','editScaleZ'].some(id=>n(id)<=0)){
   $('status').textContent='Periksa nilai posisi dan skala.';
   return;
 }
 g.position.set(n('editX'),n('editY'),n('editZ'));
 g.rotation.y=n('editRotY')*Math.PI/180;
 g.scale.set(n('editScaleX'),n('editScaleY'),n('editScaleZ'));
 $('status').textContent='Posisi elemen berhasil diperbarui.';
});
"""

anchor_js = 'function data(){'
if anchor_js not in s:
    raise SystemExit("Fungsi data() tidak ditemukan. File tidak diubah.")

s = s.replace(anchor_js, js + '\n' + anchor_js, 1)
s = s.replace(
    "extras.push(g);building.add(g);$('status').textContent=",
    "extras.push(g);building.add(g);refreshEditTargets();$('status').textContent=",
    1
)
s = s.replace(
    "building.remove(g);clear(g);$('status').textContent='Elemen terakhir dihapus.'",
    "building.remove(g);clear(g);refreshEditTargets();$('status').textContent='Elemen terakhir dihapus.'",
    1
)
s = s.replace(
    "clear(building);extras=[];let wall=",
    "clear(building);extras=[];if(typeof refreshEditTargets==='function')refreshEditTargets();let wall=",
    1
)

p.write_text(s)
print("Berhasil memasang Edit Manual 3D.")
